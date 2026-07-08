import json

with open("sidebar.json") as f:
    data = json.load(f)


def icon_html(icon):
    if icon.startswith("fa-"):
        return f'<i class="fas {icon} fa-fw"></i>'

    return f'<i class="bi {icon}"></i>'


html = []

html.append(
    '<a class="nav-link collapsed" '
    'href="#" '
    'data-bs-toggle="collapse" '
    'data-bs-target="#networkCatalogSubmenu">'
)

html.append(icon_html("bi-diagram-3"))
html.append(
    '<span class="menu-text">Network Catalog</span>'
)
html.append("</a>")

html.append(
    '<div id="networkCatalogSubmenu" '
    'class="collapse nav-dropdown-menu">'
)

html.append('<ul class="nav flex-column submenu">')

for group in data:

    group_id = (
        group["group"]
        .lower()
        .replace(" ", "_")
    )

    html.append(
        f'<li class="nav-item">'
    )

    html.append(
        f'<a class="nav-link collapsed" '
        f'data-bs-toggle="collapse" '
        f'data-bs-target="#{group_id}">'
    )

    html.append(icon_html(group["icon"]))

    html.append(
        f'<span class="menu-text">'
        f'{group["group"]}'
        f'</span>'
    )

    html.append("</a>")

    html.append(
        f'<div id="{group_id}" class="collapse submenu">'
    )

    html.append('<ul class="nav flex-column">')

    for item in group["items"]:
        html.append(
            f'<li><a href="{item["link"]}">'
            f'{item["name"]}'
            f'</a></li>'
        )

    html.append("</ul>")
    html.append("</div>")
    html.append("</li>")

html.append("</ul>")
html.append("</div>")

with open("catalog_sidebar.html", "w") as f:
    f.write("\n".join(html))

print("Generated catalog_sidebar.html")