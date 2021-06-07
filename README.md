<div align="center">
<h1>My Reddit Downloader</h1>
<h4>Download upvoted and saved media from Reddit</h4>
</div>

&nbsp; 

NOTE: This is a work in progress not all features are yet implemented. When this is ready for production this message will not be here and `myreddit-dl` will be found on PyPi

# Index

* [Requirements](#requirments)
* [Pre-Installation](#pre-installation)
* [Installation](#installation)
* [How to use](#how-to-use)
* [Advanced Configuration](#advanced-configuration)


# Requirements

- Python 3.6 or above
- requests
- praw

# Pre-Installation

[Create a developer application on reddit if needed](https://github.com/emanuel2718/myreddit-dl/blob/master/PRE_INSTALL.md)



# Installation

&nbsp; 

### 1. Clone this repository
```sh
$ git clone https://github.com/emanuel2718/myreddit-dl
$ cd myreddit-dl
```

### 2. Install requirements
```sh
$ pip install -r requirements.txt
```

### 3. Fill reddit developer app information
``` sh
$ myreddit-dl --client-config
```


# How to use
```sh
$ myreddit-dl [REQUIRED] [OPTIONS]
```

##### REQUIRED

    -U, --upvote            Download upvoted media
    -S, --saved             Download saved media


##### OPTIONS

&nbsp; 

###### Optional arguments:
    -h, --help                show this message and exit
    -v, --version             display the current version of myreddit-dl
    -verbose, --verbose       print extra information while downloading

    --sub [SUBREDDIT ...]     only download media that belongs to the given subreddit(s)
    --limit [LIMIT]           limit the amount of media to download (default: None)
    --max-depth [MAX_DEPTH]   maximum amount of posts to iterate through

    --no-video                don't download video files (.mp4, .gif, .gifv, etc.)
    --only-video              only download video files
    --nsfw                    enable NSFW content download (default: False)
    
###### Confgiguration:
    --client-config           change reddit app client information (id, secret, username, password)
    --get-config              prints the configuration file information to the terminal
    --get-config-show         prints the configuration file to the terminal and show password
    --config-prefix OPT       set filename prefix (post author username and/or post subreddit name)
                              
                              Options:
                                  '--config-prefix username'           --> username_id.ext
                                  '--config-prefix username subreddit' --> username_subreddit_id.ext
                                  '--config-prefix subreddit username' --> subreddit_username_id.ext
                                  '--config-prefix subreddit'          --> subreddit_id.ext
                                  
                              Default: subreddit --> subreddit_id.ext
                              
    --config-path PATH        path to the folder were media will be downloaded to
                              
                              Examples:
                              
                              To download the media to the folder ~/Pictures/reddit_media
                                  --config-path $HOME/Pictures/reddit_media
                                                    or
                                  --config-path ~/Picutres/reddit_media
                              
                              To download the media to the current working directory
                                  --config-path ./
                                  
                              To download the media to a folder in the current working directory
                                  --config-path ./random_folder_destination
                                  
                              Default Path: $HOME/Pictures/User_myreddit/
                                                    
    

###### Metadata:
    --save-metadata           enable this to save downloaded media metadata in a file
    --get-metadata FILE       print all the reddit metadata of the given FILE
    --get-link FILE           print reddit link of given FILE
    --get-title FILE          print post title of given FILE
    --delete-database         delete the database of the current active reddit client user

# Configuration

Set the reddit client information to be able to use myreddit-dl
``` sh
$ myreddit-dl --client-config
```

Set the path to the destination folder for the downloaded media
``` sh
$ myreddit-dl --config-path ~/Path/to/destination
```

Set the filenames prefix scheme of the downloaded media
``` sh
# This will save all the files with the scheme: `subredditName_uniqueId.extension`
$ myreddit-dl --config-prefix subreddit
```

``` sh
# This will save all the files with the scheme: `postAuthorName_uniqueId.extension`
$ myreddit-dl --config-prefix username
```

``` sh
# This will save all the files with the scheme: `subredditName_postAuthorName_uniqueId.extension`
$ myreddit-dl --config-prefix subreddit username
```

Show the current configuration
``` sh
$ myreddit-dl --get-config
```

# Usage:

Download all user upvoted media (limited to 1000 posts: Praw's API hard limit)
``` sh
$ myreddit-dl -U
```

Download all user saved media and save metadata of posts
``` sh
# This will save all the downloaded media metadata (use this flag if you want to save any of the following post data)
  # post author reddit name
  # post title
  # post link
  # post upvotes at the moment of download
  # post date of submission
$ myreddit-dl -S --save-metadata
```

Download all user upvoted and saved media and accept NSFW posts media
``` sh
$ myreddit-dl -U -S --nsfw
```

Download all the user upvoted posts from the r/MechanicalKeyboards subreddit

``` sh
$ myreddit-dl -U --sub MechanicalKeyboards
```

Download all the user upvoted posts from the r/MechanicalKeyboards and r/Battlestations subreddits

``` sh
# There's no limit to how many subreddits can be chained together
$ myreddit-dl -U --sub MechanicalKeyboards Battlestations
```

Download all the user upvoted posts from the r/MechanicalKeyboards and r/Battlestations subreddits

``` sh
$ myreddit-dl -U --sub MechanicalKeyboards Battlestations
```

Download only 10 posts media and only download images (don't download videos)

``` sh
$ myreddit-dl -U --limit 10 --no-video
```

Get the post link of a downloaded media (only if --save-metadata was used)

``` sh
# This will print the post link of that image
$ myreddit-dl --get-link random_image.png
```

Get the post title of a downloaded media (only if --save-metadata was used)

``` sh
# This will print the post title of that video
$ myreddit-dl --get-title random_video.mp4
```

Get the metadata of downloaded media (only if --save-metadata was used)

``` sh
# This will print the metadata of the image
$ myreddit-dl --get-metadata random_image.jpg
```

# TODOLIST
- [x] --max-depth argument for max number of posts to search
- [x] Make a link file (.user_links.txt)
- [x] Make a --no-video flag
- [x] use permalink to save with post title (append reddit.com)
- [x] refactor absolute_path + url from gallery_data posts...
- [x] `--only-videos` flag?
- [x] refactor entirely link saving to metadata saving for --get-metadata
- [x] `--get-metadata` --> User, title, link, user karma, sub, amount of upvotes...
- [x] `--get-title` flag in which the title of the given image is returned.
- [x] Make flag to store in either: sub_user_id.ext or user_id.ext (eliminate sub folders?)
- [x] Fix bug caused by using getcwd() in entire codebase...
- [x] Handle case where path and username are empy in `config.ini`
- [x] Refactor `filename_save` to `filename_prefix`
- [x] Allow the user to `--config-save subreddit username` for subreddit_user_id.ext
- [x] Give the user the option to insert the credentials if no credentials are found.
- [x] If config.ini is empty run script to ask user for the information
- [x] Sanitize metadata titles (remove unicode characters)
- [x] Add flag --get-path that prints the current set path and --get-filesave
- [ ] Improve loggin messages (regular and --debug)
- [ ] In advanced configuration change configparser ['REDDIT'] to desired account (--change-user).
- [ ] Make custom exceptions `exceptions.py`
- [ ] --clean-database flag that will remove all the links entries of files not longer present
- [ ] use item.link_flair_text to get tags. Some users might want items with certain tags only
- [ ] Handle case of repeated media (used --by-user and the --by-subreddit (duplicates))
- [ ] Make test suite
- [ ] Add logging of adding to path on which we are saving media
- [ ] upload to PyPy and add instruction here
- [ ] Use item.thumbnail picture for the GUI displays (maybe)
- [ ] make a last_seen.txt file and include the item that was last downloaded

