from datetime import datetime
from studentunderground.models.base import initializeDb
from studentunderground.models.base import engine
from studentunderground.db.config import DbConfig
from studentunderground.models.base import Session
from studentunderground.models.network import NetworkModel
from studentunderground.models.group import GroupModel
from studentunderground.models.user import UserModel
from studentunderground.models.profile import ProfileModel
from studentunderground.models.acl_user import AclUserModel
from studentunderground.models.acl_group import AclGroupModel
from studentunderground.models.assignment_info import AssignmentInfoModel
from studentunderground.models.assignment_content import AssignmentContentModel
from studentunderground.models.assignment_comment import AssignmentCommentModel
from studentunderground.models.article_info import ArticleInfoModel
from studentunderground.models.article_content import ArticleContentModel
from studentunderground.models.article_comment import ArticleCommentModel

class CreateTestData():
    def __init__(self):
        pass

    def createTestData(self):
        initializeDb(engine(DbConfig))
        session = Session()
        
        for k in range(0, 5):
            network = NetworkModel(name="Network" + str(k),
                                   created=datetime.now(),
                               edited=datetime.now())
        
            for i in range(0,10):
                group = GroupModel(name="Group" + str(i),
                                   created=datetime.now(),
                                   edited=datetime.now())
                
                for j in range(0, 100):
                    user = UserModel(email="Student" + str(j) + "@test.com",
                                     first_name="FirstName" + str(j),
                                     last_name="LastName" + str(j))
                    
                    acl_user = AclUserModel(email="Student" + str(j) + "@test.com",
                                            identifier="FirstName" + str(j),
                                            password="LastName" + str(j))
                    
                    profile = ProfileModel(created=datetime.now(),
                                           edited=datetime.now())
                    
                    assignment_info = AssignmentInfoModel(name="Kool Assignment" + str(j),
                                                          created=datetime.now())
                    assignment_content = AssignmentContentModel(content="Answer" + str(j),
                                                                edited=datetime.now())
                    assignment_comment = AssignmentCommentModel(content="Comment" + str(j),
                                                                created=datetime.now())

                    assignment_info.contents.append(assignment_content)
                    assignment_info.comments.append(assignment_comment)
                    group.assignments.append(assignment_info)
                    
                    article_info = ArticleInfoModel(name="Kool Assignment" + str(j),
                                                    created=datetime.now())
                    article_content = ArticleContentModel(content="Answer" + str(j),
                                                          edited=datetime.now())
                    article_comment = ArticleCommentModel(content="Comment" + str(j),
                                                          created=datetime.now())

                    article_info.contents.append(article_content)
                    article_info.comments.append(article_comment)
                    group.articles.append(article_info)
                    
                    user.acl_user = acl_user
                    user.profile = profile
                    group.users.append(user)
                    
                network.groups.append(group)
            
            session.add(network)
             
        session.commit()
        
if __name__ == '__main__':
    c = CreateTestData()
    c.createTestData()