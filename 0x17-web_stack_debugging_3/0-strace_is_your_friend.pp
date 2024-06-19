# fixing the content of a file extension in wp-settings.php

exec {'fix_phpp':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => ['/bin', 'usr/bin']
}