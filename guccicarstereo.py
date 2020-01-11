import tweepy

auth = tweepy.OAuthHandler("lD8vYvfolC6HIHRWVnOBjWsmO",
                           "U0SwAV5Nx2o0MVKr5Z6B8CgIOusomx8j9vOhqSmIzO1x6TBW19")
auth.set_access_token("1215689975062237186-CF1DKjUkDPY3EbMsuf8qSGC9fLxQZp",
                      "QHDOWYHiqR6MRbthOcoOStOs5PgoHj7KmHQqA86uSZZ4g")

api.tweepy.API(auth)

api.update_status("Lmao ya'll still using iPhones & Androids. Talk to me when you ain't broke.")