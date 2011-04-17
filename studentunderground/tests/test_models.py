import unittest
from pyramid import testing
from datetime import datetime
from studentunderground.models.base import initializeDb
from studentunderground.models.base import engine
from studentunderground.models.base import Session
from studentunderground.models.acl_user import AclUserModel
from studentunderground.models.acl_group import AclGroupModel
from studentunderground.models.assignment_info import AssignmentInfoModel
from studentunderground.models.assignment_content import AssignmentContentModel
from studentunderground.models.assignment_comment import AssignmentCommentModel
from studentunderground.models.article_info import ArticleInfoModel
from studentunderground.models.article_content import ArticleContentModel
from studentunderground.models.article_comment import ArticleCommentModel
from studentunderground.models.user import UserModel
from studentunderground.models.profile import ProfileModel
from studentunderground.models.network import NetworkModel
from studentunderground.models.group import GroupModel
from studentunderground.models.feed import FeedModel
from studentunderground.db.config import TestConfig

class TestModel(unittest.TestCase):
    def setUp(self):
        initializeDb(engine(TestConfig))

    def testBaseModel(self):
        class Config(object):
            engine = 'mysql+mysqldb'
            user = 'jayd3e'
            pw = 'sharp7&7'
            host = 'localhost'
            db = 'studentunderground_db'
            file = False

        class Config2(object):
            engine = 'sqlite'
            file = '/studentunderground/tests/studentunderground_db.db'
            user = False

        initializeDb(engine(Config))
        initializeDb(engine(Config2))
    
    def testAclUserModel(self):
        acl_user = AclUserModel(email="jayd3e@test.com",
                                identifier="jayd3e",
                                password="testpass")

        session = Session()
        session.add(acl_user)
        session.flush()

        acl_group = AclGroupModel(name="TestGroup")
        user = UserModel(email="jayd3e@test.com",
                            first_name="Bam",
                            last_name="Bamsky")
        acl_user.acl_groups.append(acl_group)
        acl_user.user = user

        self.assertTrue(str(acl_user).startswith('<AclUser'),
                        msg="str(AclUserModel) must start with '<AclUser'")
        self.assertIn(acl_user, acl_group.acl_users)
        self.assertIn(acl_group, acl_user.acl_groups)

    def testAclGroupModel(self):
        acl_group = AclGroupModel(name="TestGroup")

        session = Session()
        session.add(acl_group)
        session.flush()

        acl_user = AclUserModel(email="jayd3e@test.com",
                                identifier="jayd3e",
                                password="testpass")

        acl_group.acl_users.append(acl_user)

        self.assertTrue(str(acl_group).startswith('<AclGroup'), 
                        msg="str(AclGroupModel) must start with '<AclGroup'")
        self.assertIn(acl_user, acl_group.acl_users)
        self.assertIn(acl_group, acl_user.acl_groups)

    def testUserModel(self):
        user = UserModel(email="jayd3e@test.com",
                         first_name="Bam",
                         last_name="Bamsky")

        session = Session()
        session.add(user)
        session.flush()

        acl_user = AclUserModel(email="jayd3e@test.com",
                                identifier="jayd3e",
                                password="testpass")
        profile = ProfileModel(created=datetime.now(),
                               edited=datetime.now())
        group = GroupModel(name="Kool Course",
                           created=datetime.now(),
                           edited=datetime.now())
        network = NetworkModel(name="Kool Network",
                               created=datetime.now(),
                               edited=datetime.now())
        user.acl_user = acl_user
        user.profile = profile
        user.groups.append(group)
        user.networks.append(network)

        self.assertTrue(str(user).startswith('<User'),
                        msg="str(UserModel) must start with '<User'")
        self.assertEqual(user.acl_user, acl_user)
        self.assertEqual(acl_user.user, user)
        self.assertEqual(user.profile, profile)
        self.assertEqual(profile.user, user)
        self.assertIn(group, user.groups)
        self.assertIn(user, group.users)
        self.assertIn(network, user.networks)
        self.assertIn(user, network.users)

    def testProfileModel(self):
        user = UserModel(email="jayd3e@test.com",
                         identifier="jayd3e",
                         password="testpass")

        session = Session()
        session.add(user)
        session.flush()

        profile = ProfileModel(created=datetime.now(),
                               edited=datetime.now())
        user.profile = profile

        self.assertTrue(str(profile).startswith('<Profile'),
                        msg="str(ProfileModel) must start with '<Profile'")
        self.assertEqual(user.profile, profile)
        self.assertEqual(profile.user, user)

    def testNetworkModel(self):
        network = NetworkModel(name="School of Hard Knocks",
                               created=datetime.now(),
                               edited=datetime.now())

        group = GroupModel(name="Kool Course",
                           created=datetime.now(),
                           edited=datetime.now())

        network.groups.append(group)

        session = Session()
        session.add(network)
        session.flush()

        self.assertTrue(str(network).startswith('<Network'),
                        msg="str(NetworkModel) must start with '<Network'")
        self.assertIn(group, network.groups)
        self.assertEqual(network, group.network)
        self.assertEqual(group.network_id, network.id)

    def testGroupModel(self):
        group = GroupModel(name="Kool Course",
                           created=datetime.now(),
                           edited=datetime.now())

        network = NetworkModel(name="School of Hard Knocks",
                               created=datetime.now(),
                               edited=datetime.now())

        group.network = network

        session = Session()
        session.add(group)
        session.flush()

        self.assertTrue(str(group).startswith('<Group'),
                        msg="str(GroupModel) must start with '<Group'")
        self.assertIn(group, network.groups)
        self.assertEqual(network, group.network)
        self.assertEqual(group.network_id, network.id)

    def testAssignmentInfo(self):
        group = GroupModel(name="Kool Course",
                           created=datetime.now(),
                           edited=datetime.now())
        assignment_info = AssignmentInfoModel(name="Kool Assignment",
                                              created=datetime.now())
        assignment_content = AssignmentContentModel(content="Answer #1",
                                                    edited=datetime.now())
        assignment_comment = AssignmentCommentModel(content="Comment #1",
                                                    created=datetime.now())

        assignment_info.contents.append(assignment_content)
        assignment_info.comments.append(assignment_comment)
        group.assignments.append(assignment_info)

        session = Session()
        session.add(group)
        session.flush()

        self.assertTrue(str(assignment_info).startswith('<AssignmentInfo'),
                        msg="str(AssignmentInfoModel) must start with '<AssignmentInfoModel'")
        self.assertTrue(str(assignment_content).startswith('<AssignmentContent'),
                        msg="str(AssignmentContentModel) must start with '<AssignmentContentModel'")
        self.assertTrue(str(assignment_comment).startswith('<AssignmentComment'),
                        msg="str(AssignmentCommentModel) must start with '<AssignmentCommentModel'")
        self.assertIn(assignment_info, group.assignments)
        self.assertEqual(group, assignment_info.group)
        self.assertIn(assignment_content, assignment_info.contents)
        self.assertEqual(assignment_content.info, assignment_info)
        self.assertIn(assignment_comment, assignment_info.comments)
        self.assertEqual(assignment_comment.info, assignment_info)

    def testArticleInfo(self):
        group = GroupModel(name="Kool Course",
                           created=datetime.now(),
                           edited=datetime.now())
        article_info = ArticleInfoModel(name="Kool Assignment",
                                        created=datetime.now())
        article_content = ArticleContentModel(content="Answer #1",
                                              edited=datetime.now())
        article_comment = ArticleCommentModel(content="Comment #1",
                                              created=datetime.now())

        article_info.contents.append(article_content)
        article_info.comments.append(article_comment)
        group.articles.append(article_info)

        session = Session()
        session.add(group)
        session.flush()

        self.assertTrue(str(article_info).startswith('<ArticleInfo'),
                        msg="str(ArticleInfoModel) must start with '<ArticleInfoModel'")
        self.assertTrue(str(article_content).startswith('<ArticleContent'),
                        msg="str(ArticleContentModel) must start with '<ArticleContentModel'")
        self.assertTrue(str(article_comment).startswith('<ArticleComment'),
                        msg="str(ArticleCommentModel) must start with '<ArticleCommentModel'")
        self.assertIn(article_info, group.articles)
        self.assertEqual(group, article_info.group)
        self.assertIn(article_content, article_info.contents)
        self.assertEqual(article_content.info, article_info)
        self.assertIn(article_comment, article_info.comments)
        self.assertEqual(article_comment.info, article_info)

    def testFeedModel(self):
        feed = FeedModel(model="AssignmentModel",
                         foreign_id=1,
                         created=datetime.now())

        session = Session()
        session.add(feed)
        session.flush()

        self.assertTrue(str(feed).startswith('<Feed'),
                        msg="str(Feedmodel) must start with '<Feed'")
    
    def tearDown(self):
        testing.tearDown()
