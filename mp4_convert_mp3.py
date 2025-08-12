import streamlit as st
import subprocess
import os
import tempfile

def convert_mp4_to_mp3(input_file, output_file):
    """Convert MP4 file to MP3 using ffmpeg"""
    try:
        # Check if input file exists
        if not os.path.exists(input_file):
            st.error(f"Error: Input file '{input_file}' not found.")
            return False
        
        # Run ffmpeg command to convert MP4 to MP3
        command = [
            'ffmpeg',
            '-i', input_file,
            '-vn',  # Disable video
            '-acodec', 'libmp3lame',  # Use MP3 codec
            '-ab', '192k',  # Audio bitrate
            '-ar', '44100',  # Audio sample rate
            '-y',  # Overwrite output file if it exists
            output_file
        ]
        
        subprocess.run(command, check=True)
        st.success(f"Successfully converted to '{output_file}'")
        return True
        
    except subprocess.CalledProcessError as e:
        st.error(f"Error during conversion: {e}")
        return False
    except Exception as e:
        st.error(f"Unexpected error: {e}")
        return False

# Streamlit app
st.title("MP4 to MP3 Converter")
st.write("Upload an MP4 file to convert it to MP3")

uploaded_file = st.file_uploader("Choose an MP4 file", type=['mp4'])

if uploaded_file is not None:
    # Create temporary files
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as tmp_input:
        tmp_input.write(uploaded_file.read())
        tmp_input_path = tmp_input.name
    
    output_filename = uploaded_file.name.replace('.mp4', '.mp3')
    tmp_output_path = os.path.join(tempfile.gettempdir(), output_filename)
    
    if st.button("Convert to MP3"):
        with st.spinner("Converting..."):
            if convert_mp4_to_mp3(tmp_input_path, tmp_output_path):
                # Provide download link
                with open(tmp_output_path, 'rb') as f:
                    st.download_button(
                        label="Download MP3",
                        data=f.read(),
                        file_name=output_filename,
                        mime="audio/mpeg"
                    )
        
        # Clean up temporary files
        os.unlink(tmp_input_path)
        if os.path.exists(tmp_output_path):
            os.unlink(tmp_output_path)