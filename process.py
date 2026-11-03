import os
from moviepy.editor import VideoFileClip, ImageClip, CompositeVideoClip

TEMPLATE_PATH = "template_video.mp4"
USER_IMAGE_PATH = "user_image.jpg"  # Foydalanuvchi yuklagan rasm shu nomda saqlanadi
OUTPUT_PATH = "final_output.mp4"

def generate_video():
    if not os.path.exists(TEMPLATE_PATH):
        print("Xatolik: Shablon video topilmadi!")
        return

    if not os.path.exists(USER_IMAGE_PATH):
        print("Xatolik: Foydalanuvchi rasmi topilmadi!")
        return

    print("Video render qilinmoqda...")
    
    # Videoni yuklash
    video_clip = VideoFileClip(TEMPLATE_PATH)

    # Rasmni videoga moslash va joylash (Koordinatalarni o'z shabloningizga qarab o'zgartirasiz)
    img_clip = ImageClip(USER_IMAGE_PATH)\
        .set_duration(video_clip.duration)\
        .resize(width=200, height=200)\
        .set_position((140, 300))

    # Birlashtirish
    final_clip = CompositeVideoClip([video_clip, img_clip])
    
    # Saqlash
    final_clip.write_videofile(
        OUTPUT_PATH,
        fps=24,
        codec="libx264",
        audio_codec="aac",
        preset="ultrafast"
    )

    video_clip.close()
    final_clip.close()
    print("Video muvaffaqiyatli tayyorlandi:", OUTPUT_PATH)

if __name__ == "__main__":
    generate_video()
