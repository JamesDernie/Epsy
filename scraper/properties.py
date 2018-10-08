# Specify properties for the scraper to search for
# after making a request to the site.  General properties will
# be used unless the request is being made to a site with specified properties
# Eg youtube.com might have sight specific properties we need to look for.
# Each property contains a list of lookups. Each lookup is in the format {lookup: attribute}
# The scraper will search in order through the list
# until it finds a matching value

LINK_PROPERTIES = {
    'general': {
        'title': [
            # Facebook Open Graph
            {
                'tag': 'meta',
                'attr': 'property',
                'attr_val': 'og:title',
                'lookup': 'content',
            },
            # Twitter
            {
                'tag': 'meta',
                'attr': 'property',
                'attr_val': 'twitter:title',
                'lookup': 'content',
            },
            # Default html title tag
            {
                'tag': 'title',
                'attr': None,
                'attr_val': None,
                'lookup': None,
            },
        ],
        'description': [
            # Facebook Open Graph
            {
                'tag': 'meta',
                'attr': 'property',
                'attr_val': 'og:description',
                'lookup': 'content',
            },
            # Twitter
            {
                'tag': 'meta',
                'attr': 'property',
                'attr_val': 'twitter:description',
                'lookup': 'content',
            },
            # Meta description tag
            {
                'tag': 'meta',
                'attr': 'name',
                'attr_val': 'description',
                'lookup': 'content',
            },
        ],
        'image_url': [
            # Twitter
            {
                'tag': 'meta',
                'attr': 'property',
                'attr_val': 'twitter:image',
                'lookup': 'content',
            },
            # Facebook Open Graph
            {
                'tag': 'meta',
                'attr': 'property',
                'attr_val': 'og:image:secure_url',
                'lookup': 'content',
            },
            {
                'tag': 'meta',
                'attr': 'property',
                'attr_val': 'og:image',
                'lookup': 'content',
            },
            {
                'tag': 'link',
                'attr': 'rel',
                'attr_val': 'apple-touch-icon',
                'lookup': 'href',
            },
            {
                'tag': 'link',
                'attr': 'rel',
                'attr_val': 'icon',
                'lookup': 'href',
            }
        ],
        'content_url': [],
    },
    'reddit': {
        'content_url': [
            # Twitter
            {
                'tag': 'meta',
                'attr': 'property',
                'attr_val': 'twitter:image',
                'lookup': 'content',
            },
            # Facebook Open Graph
            {
                'tag': 'meta',
                'attr': 'property',
                'attr_val': 'og:image:secure_url',
                'lookup': 'content',
            },
            {
                'tag': 'meta',
                'attr': 'property',
                'attr_val': 'og:image',
                'lookup': 'content',
            },
            {
                'tag': 'link',
                'attr': 'rel',
                'attr_val': 'apple-touch-icon',
                'lookup': 'href',
            },
            {
                'tag': 'link',
                'attr': 'rel',
                'attr_val': 'icon',
                'lookup': 'href',
            }
        ],
    }
}
