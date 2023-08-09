# puppet file to automate a 500 error fix
# A 'phpp' instead of a 'php' string found and corrected
exec { 'fixed-phpp-typo-error':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => '/bin';
}
