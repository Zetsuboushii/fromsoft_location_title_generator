import svgwrite


def create_svg_with_caption(caption, output_file):
    width = 1000
    height = 200
    font_size = 48
    font_family = 'serif'

    dwg = svgwrite.Drawing(output_file, profile='tiny', size=(width, height), debug=True)

    text_x = width // 2
    text_y = height // 2 + font_size // 3

    dwg.add(dwg.text(
        caption,
        insert=(text_x, text_y),
        text_anchor="middle",
        font_size=font_size,
        font_family=font_family,
        fill="white"
    ))

    line_y = text_y + 10
    path_d = f"M {text_x - 375} {line_y} Q {text_x} {line_y-1}, {text_x + 375} {line_y}"

    # Create the gradient for the line
    gradient = dwg.linearGradient((0, 0), (1, 0), id="fade")
    gradient.add_stop_color(0, "white", opacity=0)
    gradient.add_stop_color(0.5, "white", opacity=1)
    gradient.add_stop_color(1, "white", opacity=0)
    dwg.defs.add(gradient)

    dwg.add(dwg.path(
        d=path_d,
        stroke="url(#fade)",
        stroke_width=2,
        fill="none"
    ))

    dwg.save()


if __name__ == "__main__":
    # Get name input from the user
    name = input("Enter a name: ")

    # Specify the output file
    output_file = "caption_with_fading_line.svg"

    # Create and save the SVG with the given name
    create_svg_with_caption(name, output_file)
    print(f"SVG saved as {output_file}")
