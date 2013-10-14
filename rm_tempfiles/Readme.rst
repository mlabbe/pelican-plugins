RM Tempfiles
------------

Given a list of temporary file extensions, prune them from the output directory.

Put this in the plugin list before any plugins that further process files
in the output directory, such as ``gzip_cache``.
