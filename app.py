
import gradio as gr

from src.bible_agent.crew import BibleAgent



import time

def run_crew(topic, bible_version):
    """
    Main function to run the Bible Project crew analysis
    """
    inputs = {
        'topic': topic,
        'bible_version': bible_version
    }
    
    # Add some processing indication
    yield "🔍 Analyzing your topic and gathering insights..."
    time.sleep(1)
    
    # Your existing crew logic here
    project = BibleAgent()
    crew = project.crew()
    results = crew.kickoff(inputs=inputs)
    
    yield results

# Custom CSS for beautiful styling
custom_css = """
/* Main container styling */
.gradio-container {
    background-image: linear-gradient(60deg, #29323c 0%, #485563 100%);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

/* Header styling */
.header-container {
    text-align: center;
    padding: 2rem;
    background: rgba(255, 255, 255, 0.1);
    border-radius: 15px;
    margin-bottom: 2rem;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.2);
}

/* Input section styling */
.input-section {
    background: rgba(255, 255, 255, 0.95);
    border-radius: 15px;
    padding: 2rem;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    margin-bottom: 1rem;
}

/* Output section styling */
.output-section {
    background: linear-gradient(-180deg, #BCC5CE 0%, #929EAD 98%), radial-gradient(at top left, rgba(255,255,255,0.30) 0%, rgba(0,0,0,0.30) 100%);
    background-blend-mode: screen;
    border-radius: 7px;
    padding: 1rem;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    margin-top: 1rem;
}

/* Button styling */
.submit-btn {
    background: linear-gradient(45deg, #4CAF50, #45a049);
    color: white;
    border: none;
    padding: 12px 30px;
    border-radius: 0px;
    font-size: 16px;
    font-weight: bold;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(76, 175, 80, 0.3);
}

.submit-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(76, 175, 80, 0.4);
}

/* Input field styling */
.input-field {
    border: 2px solid #e0e0e0;
    border-radius: 10px;
    padding: 12px;
    font-size: 14px;
    transition: border-color 0.3s ease;
}

.input-field:focus {
    border-color: #667eea;
    box-shadow: 0 0 10px rgba(102, 126, 234, 0.3);
}

/* Title styling */
.title {
    color: white;
    font-size: 2.5rem;
    font-weight: bold;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
    margin-bottom: 0.5rem;
}

.subtitle {
    color: rgba(255, 255, 255, 0.9);
    font-size: 1.1rem;
    margin-bottom: 1rem;
}

/* Loading animation */
@keyframes pulse {
    0% { opacity: 1; }
    50% { opacity: 0.5; }
    100% { opacity: 1; }
}

.loading {
    animation: pulse 2s infinite;
}
"""

# Bible versions for dropdown
bible_versions = [
    "KJV - King James Version",
    "NKJV - New King James Version",
    "NLT - New Living Translation",
    "NIV - New International Version",
]

# Create the enhanced interface
with gr.Blocks(css=custom_css, title="Bible Project Insights") as iface:
    
    # Header section
    with gr.Row():
        with gr.Column():
            gr.HTML("""
                <div class="header-container">
                    <h1 class="title">📖 Bible Project Insights</h1>
                    <p class="subtitle">Discover deep biblical insights and wisdom through AI-powered analysis</p>
                    <p style="color: rgba(255, 255, 255, 0.8); font-size: 0.9rem;">
                        Enter any topic or question, select your preferred Bible version, and let our crew of agents provide you with comprehensive biblical insights.
                    </p>
                </div>
            """)
    
    # Main content area
    with gr.Row():
        # Input section
        with gr.Column(scale=1):
            with gr.Group():
                gr.HTML('<div style="text-align: center; margin-bottom: 1rem;"><h3 style="color: #FFFFFF; margin: 0;">🔍 Your Inquiry</h3></div>')
                
                topic_input = gr.Textbox(
                    label="📝 Topic or Question",
                    placeholder="e.g., 'What does the Bible say about love?', 'Parables of Jesus', 'Faith and works'...",
                    lines=3,
                    elem_classes="input-field"
                )
                
                version_input = gr.Dropdown(
                    label="📚 Bible Version",
                    choices=bible_versions,
                    value="KJV - King James Version",
                    elem_classes="input-field"
                )
                
                with gr.Row():
                    submit_btn = gr.Button(
                        "✨ Get Biblical Insights",
                        variant="primary",
                        size="lg",
                        elem_classes="submit-btn"
                    )
                    clear_btn = gr.Button(
                        "🗑️ Clear",
                        variant="secondary",
                        size="lg"
                    )
    
    # Output section
    with gr.Row():
        with gr.Column():
            gr.HTML('<div style="text-align: center; margin: 1rem 0;"><h3 style="color: #FFFFFF;">📜 Biblical Insights & Analysis</h3></div>')

            output_text = gr.Textbox(
                label="Results",
                lines=15,
                show_label=False,
                elem_classes="output-section",
                placeholder="Your biblical insights will appear here...",
                interactive=False
            )
    
    # Examples section
    with gr.Row():
        gr.Examples(
            examples=[
                ["What does the Bible teach about forgiveness?", "NIV - New International Version"],
                ["The meaning of Psalm 23", "NKJV - New King James Version"],
                ["Jesus' teachings on prayer", "KJV - King James Version"],
                ["Biblical perspective on anxiety and worry", "NLT - New Living Translation"]
            ],
            inputs=[topic_input, version_input],
            label="💡 Try these example topics:"
        )
    
    # Footer
    gr.HTML("""
        <div style="text-align: center; margin-top: 2rem; padding: 1rem; 
                    background: rgba(255, 255, 255, 0.1); border-radius: 10px; 
                    backdrop-filter: blur(10px);">
            <p style="color: rgba(255, 255, 255, 0.8); margin: 0;">
                🙏 May this tool help you grow in understanding and faith
            </p>
        </div>
    """)
    
    # Event handlers
    submit_btn.click(
        fn=run_crew,
        inputs=[topic_input, version_input],
        outputs=output_text,
        show_progress=True
    )
    
    clear_btn.click(
        lambda: ["", "KJV - King James Version", ""],
        outputs=[topic_input, version_input, output_text]
    )

# Launch configuration
if __name__ == "__main__":
    iface.launch(
        share=False,  # Set to True if you want to create a public link
        debug=False
    )