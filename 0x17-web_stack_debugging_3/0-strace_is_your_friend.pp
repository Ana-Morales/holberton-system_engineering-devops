# Fix typo in wp-settings file
exec { 'Fixing error':
  command => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  path    => '/bin/'
  }
