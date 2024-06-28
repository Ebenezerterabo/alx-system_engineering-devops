# fixing request failed

exec {'fixing user_limit':
        command => "sed -i 's/15/4096/' /etc/default/nginx && sudo service nginx restart",
        path    => ['usr/bin', 'sbin', 'bin'],
}
