import io
import streamlit as st
from PIL import Image

from image_utils import encode_image, decode_image
from text_utils import encode_text, decode_text
from utils import evaluate, get_download_bytes


# ========================================================
# PAGE CONFIGURATION
# ========================================================

st.set_page_config(
    page_title="Deep Learning Steganography",
    page_icon="🔒",
    layout="wide"
)


# ========================================================
# HEADER
# ========================================================

st.markdown(
    """
    <div style="
        background: linear-gradient(135deg, #4F46E5, #06B6D4);
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 30px;
    ">
        <h1 style="
            color: white;
            font-size: 42px;
            font-weight: 700;
            margin-bottom: 10px;
        ">
            🔒 Deep Learning Steganography
        </h1>

        <p style="
            color: white;
            font-size: 20px;
            margin: 0;
        ">
            Hide sensitive information inside images using Deep Learning and Encryption.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()


# ========================================================
# SELECT MODE
# ========================================================

mode = st.radio(
    "Choose Mode",
    (
        "🖼️ Image Steganography",
        "📝 Text Steganography"
    ),
    horizontal=True
)

st.divider()


# ========================================================
# IMAGE STEGANOGRAPHY
# ========================================================

if mode == "🖼️ Image Steganography":

    operation = st.radio(
        "Choose Operation",
        (
            "🔐 Encode",
            "🔓 Decode"
        ),
        horizontal=True,
        key="image_operation"
    )

    st.divider()


    # ====================================================
    # IMAGE ENCODE
    # ====================================================

    if operation == "🔐 Encode":

        st.subheader("🔐 Hide Image Inside Another Image")

        cover = st.file_uploader(
            "Upload Cover Image",
            type=["png", "jpg", "jpeg"],
            key="cover"
        )

        secret = st.file_uploader(
            "Upload Secret Image",
            type=["png", "jpg", "jpeg"],
            key="secret"
        )

        if st.button(
            "🔐 Encode Image",
            use_container_width=False
        ):

            if cover is None or secret is None:

                st.warning(
                    "⚠️ Please upload both Cover Image and Secret Image."
                )

            else:

                try:

                    # Load images
                    cover_img = Image.open(cover).convert("RGB")
                    secret_img = Image.open(secret).convert("RGB")

                    with st.spinner(
                        "🤖 AI model is encoding your images... Please wait."
                    ):

                        (
                            stego,
                            recovered,
                            cover_tensor,
                            secret_tensor,
                            stego_tensor,
                            recovered_tensor
                        ) = encode_image(
                            cover_img,
                            secret_img
                        )

                    st.success(
                        "✅ Image Encoding Completed Successfully!"
                    )


                    # ====================================
                    # METRICS
                    # ====================================

                    metrics = evaluate(
                        cover_tensor,
                        secret_tensor,
                        stego_tensor,
                        recovered_tensor
                    )

                    st.subheader("📊 Quality Metrics")

                    col1, col2 = st.columns(2)

                    with col1:

                        st.metric(
                            "Cover → Stego PSNR",
                            f"{metrics['cover_psnr']} dB"
                        )

                        st.metric(
                            "Cover → Stego SSIM",
                            metrics["cover_ssim"]
                        )

                    with col2:

                        st.metric(
                            "Secret → Recovered PSNR",
                            f"{metrics['secret_psnr']} dB"
                        )

                        st.metric(
                            "Secret → Recovered SSIM",
                            metrics["secret_ssim"]
                        )


                    # ====================================
                    # IMAGE COMPARISON
                    # ====================================

                    st.divider()

                    st.subheader("🖼️ Image Comparison")

                    c1, c2, c3, c4 = st.columns(4)

                    with c1:

                        st.image(
                            cover_img,
                            caption="Cover Image",
                            use_container_width=True
                        )

                    with c2:

                        st.image(
                            secret_img,
                            caption="Secret Image",
                            use_container_width=True
                        )

                    with c3:

                        st.image(
                            stego,
                            caption="Stego Image",
                            use_container_width=True
                        )

                    with c4:

                        st.image(
                            recovered,
                            caption="Recovered Secret",
                            use_container_width=True
                        )


                    # ====================================
                    # DOWNLOAD
                    # ====================================

                    st.divider()

                    st.download_button(
                        label="📥 Download Stego Image",
                        data=get_download_bytes(stego),
                        file_name="stego_image.png",
                        mime="image/png"
                    )


                except FileNotFoundError as e:

                    st.error(
                        "❌ Model checkpoint file was not found."
                    )

                    st.code(str(e))


                except RuntimeError as e:

                    st.error(
                        "❌ Deep Learning model error."
                    )

                    st.code(str(e))


                except Exception as e:

                    st.error(
                        "❌ Unexpected error while encoding images."
                    )

                    st.code(str(e))


    # ====================================================
    # IMAGE DECODE
    # ====================================================

    else:

        st.subheader("🔓 Recover Hidden Image")

        stego_file = st.file_uploader(
            "Upload Stego Image",
            type=["png", "jpg", "jpeg"],
            key="decode_image"
        )

        if st.button(
            "🔓 Decode Image"
        ):

            if stego_file is None:

                st.warning(
                    "⚠️ Please upload a Stego Image."
                )

            else:

                try:

                    stego_img = Image.open(
                        stego_file
                    ).convert("RGB")

                    with st.spinner(
                        "🤖 AI model is recovering the hidden image..."
                    ):

                        recovered = decode_image(
                            stego_img
                        )

                    st.success(
                        "✅ Secret Image Recovered Successfully!"
                    )

                    col1, col2 = st.columns(2)

                    with col1:

                        st.image(
                            stego_img,
                            caption="Stego Image",
                            use_container_width=True
                        )

                    with col2:

                        st.image(
                            recovered,
                            caption="Recovered Secret Image",
                            use_container_width=True
                        )


                except FileNotFoundError as e:

                    st.error(
                        "❌ Model checkpoint file was not found."
                    )

                    st.code(str(e))


                except RuntimeError as e:

                    st.error(
                        "❌ Deep Learning model error."
                    )

                    st.code(str(e))


                except Exception as e:

                    st.error(
                        "❌ Unexpected error while decoding the image."
                    )

                    st.code(str(e))


# ========================================================
# TEXT STEGANOGRAPHY
# ========================================================

else:

    operation = st.radio(
        "Choose Operation",
        (
            "🔐 Encode",
            "🔓 Decode"
        ),
        horizontal=True,
        key="text_operation"
    )

    st.divider()


    # ====================================================
    # TEXT ENCODE
    # ====================================================

    if operation == "🔐 Encode":

        st.subheader("🔐 Hide Text Inside an Image")

        cover = st.file_uploader(
            "Upload Cover Image",
            type=["png", "jpg", "jpeg"],
            key="text_cover"
        )

        message = st.text_area(
            "Secret Message",
            placeholder="Enter your secret message here..."
        )

        password = st.text_input(
            "Password (Optional)",
            type="password",
            key="encode_password"
        )


        if st.button(
            "🔐 Encode Message"
        ):

            if cover is None:

                st.warning(
                    "⚠️ Please upload a Cover Image."
                )

            elif not message.strip():

                st.warning(
                    "⚠️ Please enter a secret message."
                )

            else:

                try:

                    image = Image.open(
                        cover
                    ).convert("RGB")

                    with st.spinner(
                        "🔐 Hiding your message inside the image..."
                    ):

                        stego = encode_text(
                            image.copy(),
                            message,
                            password
                        )

                    st.success(
                        "✅ Message Encoded Successfully!"
                    )


                    col1, col2 = st.columns(2)

                    with col1:

                        st.image(
                            image,
                            caption="Original Image",
                            use_container_width=True
                        )

                    with col2:

                        st.image(
                            stego,
                            caption="Stego Image",
                            use_container_width=True
                        )


                    # Download
                    buffer = io.BytesIO()

                    stego.save(
                        buffer,
                        format="PNG"
                    )

                    st.download_button(
                        label="📥 Download Stego Image",
                        data=buffer.getvalue(),
                        file_name="stego_text.png",
                        mime="image/png"
                    )


                except ValueError as e:

                    st.error(
                        f"❌ {str(e)}"
                    )


                except Exception as e:

                    st.error(
                        "❌ Error while encoding the message."
                    )

                    st.code(str(e))


    # ====================================================
    # TEXT DECODE
    # ====================================================

    else:

        st.subheader("🔓 Recover Hidden Message")

        stego_file = st.file_uploader(
            "Upload Stego Image",
            type=["png", "jpg", "jpeg"],
            key="text_decode"
        )

        password = st.text_input(
            "Password (Optional)",
            type="password",
            key="decode_password"
        )


        if st.button(
            "🔓 Decode Message"
        ):

            if stego_file is None:

                st.warning(
                    "⚠️ Please upload a Stego Image."
                )

            else:

                try:

                    image = Image.open(
                        stego_file
                    ).convert("RGB")

                    with st.spinner(
                        "🔍 Extracting hidden message..."
                    ):

                        message = decode_text(
                            image,
                            password
                        )


                    if message.startswith("❌"):

                        st.error(message)

                    elif message.startswith("🔐"):

                        st.warning(message)

                    else:

                        st.success(
                            "✅ Message Recovered Successfully!"
                        )

                        st.text_area(
                            "Recovered Message",
                            value=message,
                            height=180
                        )


                    st.image(
                        image,
                        caption="Stego Image",
                        use_container_width=True
                    )


                except Exception as e:

                    st.error(
                        "❌ Error while decoding the message."
                    )

                    st.code(str(e))
