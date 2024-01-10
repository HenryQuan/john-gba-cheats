# John GBA Cheats
John GBA is a much cheaper GBA emulator for Android. It uses its own XML format for cheats. This repo contains a script to convert other cheat formats to John GBA's format.

## Format
The format is in XML. The root element is `<cheats>`, then it has a list of `<item>` elements. Each `<item>` element has `disabled`, `name`, and `code` attributes. The `disabled` attribute is either `true` or `false`. The `code` attribute is the cheat code, and `&#` is used to represent a newline.

