from PIL import Image, ImageDraw, ImageFont


def make_watermark(watermark_name: str, image_file: str, outputDirectory: str):
    with Image.open(image_file).convert("RGBA") as base:
        # make a blank image for the text, initialized to transparent text color
        txt = Image.new("RGBA", base.size, (255, 255, 255, 0))

        # get a font
        fnt = ImageFont.truetype("Rubik-Regular.ttf", 500)
        fnt_2 = ImageFont.truetype("Rubik-Regular.ttf", 150)
        # get a drawing context
        d = ImageDraw.Draw(txt)

        # draw text, half opacity
        d.text((1808.5, 2862.5), watermark_name, font=fnt, fill=(255, 255, 255, 100))
        d.text((1808.5, 3500.5), f"{watermark_name}.com", font=fnt_2, fill=(255, 255, 255, 100))

        out = Image.alpha_composite(base, txt)
        out.save(f"{outputDirectory}/watermark.png")


path = 'C:/Users/hp/Pictures/dosse/mani/Designers blog/style.jpg'
split_path = path.split("/")
split_path.pop()
directory =  "/".join(split_path)
