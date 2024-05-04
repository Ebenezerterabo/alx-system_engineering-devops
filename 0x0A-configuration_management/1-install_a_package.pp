# Install flask using the pip3

package {'flask':
    ensure   => present,
    provider => 'pip3',
}