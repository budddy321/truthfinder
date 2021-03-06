from django.db import models
from richtext.fields import AdminRichTextField

class TruthNode(models.Model):
    title = models.CharField(max_length=200, db_index=True,
        verbose_name="Claim")
    content = AdminRichTextField(max_length=20000, blank=True, 
        verbose_name="Explanation")
    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title
    
class NodeRelationship(models.Model):
    PRO, CON, PREMISE = range(3)
    RELATIONSHIP_CHOICES = (
        (PRO, u'Pro'),
        (CON, u'Con'),
        (PREMISE, u'Premise'),
    )
    parent_node = models.ForeignKey(TruthNode,
        related_name="noderelationship_parent_set")
    child_node = models.ForeignKey(TruthNode,
        related_name="noderelationship_child_set")
    # child's relationship to parent
    relationship = models.IntegerField(choices=RELATIONSHIP_CHOICES)

    # if True, child has an inverse relationship with parent
    invert_child = models.BooleanField(default=False)

    # the meta-node to discuss whether this relationship is good
    discussion_node = models.ForeignKey(TruthNode, null=True, blank=True,
        related_name="noderelationship_discussion_set")

class ChangeNotification(models.Model):
    PIN, UNPIN, CREATE, DELETE, EDIT, ADD = range(6)
    NOTIFICATION_CHOICES = (
        # <user> pinned <node> as a <pin_type> to <parent>
        (PIN, u'Pin'),
        # <user> unpinned <node> as a <pin_type> from <parent>
        (UNPIN, u'Unpin'),
        # <user> created <node>
        (CREATE, u'Create'),
        # <user> deleted <node_title>
        (DELETE, u'Delete'),
        # <user> edited <node>
        (EDIT, u'Edit'),
        # <user> added <node> as a <pin_type> to <parent>
        (ADD, u'Add'),
    )
    # when the change occurred
    date = models.DateTimeField(auto_now_add=True, db_index=True)
    # which kind of notification
    change_type = models.IntegerField(choices=NOTIFICATION_CHOICES)
    # person who caused the change
    user = models.CharField(max_length=100, blank=True, null=True)
    # target node / child node
    node = models.ForeignKey(TruthNode, blank=True, null=True, 
        related_name="changenotification_node_set")
    node_title = models.CharField(max_length=200, blank=True, null=True)
    # target node 2 / parent node
    parent_node = models.ForeignKey(TruthNode, blank=True, null=True,
        related_name="changenotification_parent_node_set")
    parent_node_title = models.CharField(max_length=200, blank=True, null=True)
    pin_type = models.IntegerField(choices=NodeRelationship.RELATIONSHIP_CHOICES, blank=True, null=True)
    
class User(models.Model):
    INACTIVE, ACTIVE, BANNED = range(3)
    STATUS_CHOICES = (
        (INACTIVE, 'Registered'),
        (ACTIVE, 'Active'),
        (BANNED, 'Banned'),
    )
    email = models.EmailField(db_index=True)
    activate_code = models.CharField(max_length=100)
    status = models.IntegerField(choices=STATUS_CHOICES, default=INACTIVE)
