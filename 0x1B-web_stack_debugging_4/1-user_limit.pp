# fixing too many files (holberton soft)

exec { 'fix holberton soft':
    command => "sed -i '/holberton soft/s/4/10000/' /etc/security/limits.conf",
    path    => ['/usr/bin', '/usr/local/bin', '/sbin', '/bin'],
}

# fixing too many files (holberton hard)

exec { 'fix holberton hard':
    command => "sed -i '/holberton hard/s/5/10000/' /etc/security/limits.conf",
    path    => ['/usr/bin', '/usr/local/bin', '/sbin', '/bin'],
}
