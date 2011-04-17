<%namespace name="header" file="header.mako"/>
<%namespace name="footer" file="footer.mako"/>
<!-- base.mako --> 
<!DOCTYPE html>
<html>
    <head>
        <title>${title}</title>
        <link rel="stylesheet" type="text/css" href="/static/css/reset.css" />
        <link rel="stylesheet" type="text/css" href="/static/css/style.css" />
        <link rel="stylesheet" type="text/css" href="/static/css/type.css" />
    </head>
    <body>
        <div class="header">
            ${header.header(here)}
        </div>
        <div class="main">
            <fieldset class="body">
                <legend>Content</legend>
                ${self.body()}
            </fieldset>
        </div>
        <div class="side">
                    
        </div>
        <div class="footer">
            ${footer.footer()}
        </div>
    </body>
</html>
