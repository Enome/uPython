#Snippet file for all other python files
#To uncomment in VS2010: hold ctrl type k type u 

try:
    import sys
    import clr
    
    #Python directory
    #clr.AddReference('System.Web')
    #from System.Web.HttpContext import Current
    #sys.path.append(Current.Server.MapPath('~/python'))

    #Node
    #from umbraco.presentation.nodeFactory import Node

    #Media
    #clr.AddReference('cms')
    #clr.AddReference('businesslogic')
    #from umbraco.cms.businesslogic.media import Media

    #Utils
    #from utils import get_property
    
    #Generate Html
    def generate(currentPage):
        return 'snippet file works'

    # The following code makes it possible to use this 
    # module in other modules
    try: currentPage
    except Exception: currentPage = None

    if currentPage:
        print generate(currentPage)
            
except:
  print sys.exc_info()