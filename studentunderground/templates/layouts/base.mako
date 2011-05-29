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
            <div class="main">
                ${header.header(here)}
            </div>
        </div>
        <div class="body">
            <div class="main">
                <div class="mainbar">
                    <fieldset>
                        <legend>${legend}</legend>
                        ${self.mainbar()}
                    </fieldset>
                </div>
                <div class="sidebar">
                    ${self.sidebar()}            
                </div>
            </div>
        </div>
        <div class="footer">
            <div class="main">
                ${footer.footer()}
            </div>
        </div>
    </body>
</html>
