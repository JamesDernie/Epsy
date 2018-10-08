from urllib.parse import urlparse, urljoin
import re


from .properties import LINK_PROPERTIES


def scrape(soup, url):
    data = {}

    parsed_uri = urlparse(url)
    site_name = re.sub(r'(www.|.com)', '', string='{uri.netloc}'.format(uri=parsed_uri))

    properties = LINK_PROPERTIES['general']

    try:
        special_properties = LINK_PROPERTIES[site_name.lower()]
    except IndexError:
        special_properties = None

    # Loop through properties
    for prop, lookups in properties.items():
        # Loop through different lookups (l) for each property.
        # If lookup is found, break
        p_val = None
        for l in lookups:
            tag = soup.find(l['tag'], attrs={l['attr']: l['attr_val']} if l['attr'] else None)
            if tag:
                lookup_key = l['lookup']
                if lookup_key:
                    try:
                        p_val = tag.attrs[lookup_key]
                    except (AttributeError, KeyError):
                        pass
                else:
                    p_val = tag.string
            if p_val:
                break

        data[prop] = p_val

        # Add domain to data
        data['domain'] = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)

    return data









