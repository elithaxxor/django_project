from browser import document, prompt, html, alert
 2import base64
 3
 4b64_map = {}
 5
 6def base64_compute(_):
 7    value = document["text-src"].value
 8    if not value:
 9        alert("You need to enter a value")
10        return
11    if value in b64_map:
12        alert(f"'The base64 value of '{value}' already exists: '{b64_map[value]}'")
13        return
14    b64data = base64.b64encode(value.encode()).decode()
15    b64_map[value] = b64data
16    display_map()
17
18def clear_map(_) -> None:
19    b64_map.clear()
20    document["b64-display"].clear()
21
22def display_map() -> None:
23    table = html.TABLE(Class="pure-table")
24    table <= html.THEAD(html.TR(html.TH("Text") + html.TH("Base64")))
25    table <= (html.TR(html.TD(key) + html.TD(b64_map[key])) for key in b64_map)
26    base64_display = document["b64-display"]
27    base64_display.clear()
28    base64_display <= table
29    document["text-src"].value = ""
30
31document["submit"].bind("click", base64_compute)
32document["clear-btn"].bind("click", clear_map)