from datetime import datetime
from studentunderground.models.base import initializeDb
from studentunderground.models.base import engine
from studentunderground.db.config import DbConfig
from studentunderground.models.base import Session
from studentunderground.models.feed import FeedModel
from studentunderground.models.profile import ProfileModel
from studentunderground.models.network import NetworkModel
from studentunderground.models.group import GroupModel
from studentunderground.models.user import UserModel
from studentunderground.models.user import UserGroupModel
from studentunderground.models.user import UserNetworkModel
from studentunderground.models.acl_user import AclUserModel
from studentunderground.models.acl_group import AclGroupModel
from studentunderground.models.assignment_info import AssignmentInfoModel
from studentunderground.models.assignment_content import AssignmentContentModel
from studentunderground.models.assignment_comment import AssignmentCommentModel
from studentunderground.models.article_info import ArticleInfoModel
from studentunderground.models.article_content import ArticleContentModel
from studentunderground.models.article_comment import ArticleCommentModel

class DeleteAll():
    def __init__(self):
        pass

    def deleteAll(self):
        initializeDb(engine(DbConfig))
        session = Session()
        
        session.execute(UserGroupModel.delete('1=1'))
        session.execute(UserNetworkModel.delete('1=1'))
        session.query(ProfileModel).delete() 
        session.query(AssignmentInfoModel).delete() 
        session.query(AssignmentContentModel).delete() 
        session.query(AssignmentCommentModel).delete() 
        session.query(ArticleInfoModel).delete() 
        session.query(ArticleContentModel).delete() 
        session.query(ArticleCommentModel).delete() 
        session.query(UserModel).delete() 
        session.query(AclUserModel).delete() 
        session.query(GroupModel).delete() 
        session.query(AclGroupModel).delete() 
        session.query(NetworkModel).delete() 
        session.query(FeedModel).delete() 
        
        session.commit()
        
if __name__ == '__main__':
    c = DeleteAll()
    c.deleteAll()
