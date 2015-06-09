## Default flow

   1. Load the config file
   2. check for the available renderable documents
      - create objects to render
   3. check for available rendrable posts
      - create objects to render
   4. create required directories in destination directoy.
   5. render and create nessecory html pages.


## Config file details

   This will be json file
   
   <pre>
   {
	title: "Site Title",
	author: "Author of the site", // this is the primary author of the site
	site_url: "http://`<sitename>`.`<tld>`"
   }
   </pre>



## Rendering Documents/Posts
   
   Before rendering the docs/post load the rendering engine.

## Create directories
   
   based on documents and post categories create required directories.

## Python Dictionary structure expected

      """
      example structure 
      {
          "Site" : {
              "title": "Zeorth.me",
              "url":"http://zeroth.me",
              pages:{
              documents:[
              {"document":{
                  "title":"About",
                  "date":"2015-12-4",
                  "body":"something",
                  "header":{
                      "title":"about"
                  }
              }}],
              directories:[
                 {
                    "directory":{
                        "title":"main",
                        "documents":[
                            {
                               "document":{
                                   "title":"About1",
                                   "date":"2015-12-4",
                                   "body":"something",
                                   "header":{
                                       "title":"about"
                                   }
                               }
                            },
                            {
                               "document":{
                                   "title":"About2",
                                   "date":"2015-12-4",
                                   "body":"something",
                                   "header":{
                                       "title":"about"
                                   }
                               }
                            }
                        ]
                    }
                 }
              ]
           }
          }
      }
      """