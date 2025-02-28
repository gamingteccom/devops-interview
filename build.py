import os
import sys


if os.path.exists('.git') and os.environ.get("APP_ENV") == "production":
    print("SECURITY CHECK FAILED!")
    print("Please do not keep the .git directory in the image!")
    sys.exit(1)

TEXT = """<!DOCTYPE html>
<html>
    <head>
        <title>PHP Test</title>
    </head>
    <body>
        <?php echo '<p>Hello World</p>'; ?>
    </body>
</html>
"""

if not os.path.exists('public'):
    os.mkdir('public')
with open('public/index.php', 'w') as f:
    f.write(TEXT)
