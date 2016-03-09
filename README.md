# skeleton
A Pelican theme styled with Skeleton

## Dependecies

The Theme depends on ``sort_tags``. If the plugin is not available, the
fallback behaviour is to sort the tags by name.

## Impressum

If you need to include an impressum on your page, you can set
``SKELETON_DISPLAY_IMPRESSUM`` to ``True``. The impressum page itself has to be a page
in the Pelican sense and has to be named ``impressum.md``. Take care to also
set ``status: hidden`` in order to hide it from the rest of the blog.

## Newsletter signup

If you want to allow users to sign up for a newsletter, you can activate the
``SKELETON_NEWSLETTER_SIGNUP`` switch. As with the impressum you will have to
create a hidden ``newsletter_signup.md`` page.

## SkeletonImages plugin

The plugin orientation in the SkeletonImages package can be used to add the
classes `landscape, square, portrait, portrait32, portrait43, portrait54` to
image tags in order to make their responsive scaling work as defined in the
`mystyle.css`.

## Colophon
This theme is based on the `simple` theme of
[Pelican](https://github.com/getpelican/pelican). The css styling was performed
using [Skeleon](https://github.com/dhg/Skeleton).
