import markdown
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Image
from reportlab.lib.units import inch
from reportlab.lib import colors
import os
import re

def markdown_to_pdf_with_signature(input_md_file, output_pdf_file, author_name="Pedro Musculini"):
    """Convert Markdown file to PDF with author signature, logo, and charts using ReportLab"""

    # Read the markdown file
    with open(input_md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Add signature to the end of the article
    signature_block = f"""

---

**Author:** {author_name}
**Date:** September 15, 2025
**Project:** NYC Taxi Data Enrichment Pipeline
**Contact:** [Your contact information here]

*This article was created as part of the NYC Taxi Data Enrichment Pipeline project, demonstrating advanced feature engineering techniques for urban transportation analytics.*
"""

    # Append signature to markdown content
    md_content_with_signature = md_content + signature_block

    # Convert markdown to HTML first, then extract text content
    html_content = markdown.markdown(md_content_with_signature, extensions=['tables', 'fenced_code'])

    # Clean HTML tags for PDF generation
    clean_text = re.sub(r'<[^>]+>', '', html_content)
    clean_text = re.sub(r'&[^;]+;', ' ', clean_text)

    # Split content into sections
    sections = clean_text.split('\n\n')

    # Create PDF document
    doc = SimpleDocTemplate(output_pdf_file, pagesize=A4,
                           rightMargin=72, leftMargin=72,
                           topMargin=72, bottomMargin=72)
    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=30,
        alignment=1,  # Center alignment
        textColor=colors.darkblue,
        fontName='Helvetica-Bold'
    )

    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Normal'],
        fontSize=14,
        spaceAfter=20,
        alignment=1,
        textColor=colors.darkblue,
        fontName='Helvetica-Bold'
    )

    heading2_style = ParagraphStyle(
        'CustomHeading2',
        parent=styles['Heading2'],
        fontSize=18,
        spaceAfter=20,
        textColor=colors.darkblue,
        borderColor=colors.blue,
        borderWidth=2,
        borderPadding=5,
        leftIndent=10,
        fontName='Helvetica-Bold'
    )

    heading3_style = ParagraphStyle(
        'CustomHeading3',
        parent=styles['Heading3'],
        fontSize=14,
        spaceAfter=15,
        textColor=colors.darkblue,
        fontName='Helvetica-Bold'
    )

    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=12,
        spaceAfter=12,
        leading=16,
        fontName='Helvetica'
    )

    code_style = ParagraphStyle(
        'CustomCode',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=10,
        backColor=colors.lightgrey,
        borderColor=colors.grey,
        borderWidth=1,
        borderPadding=5,
        leftIndent=20,
        rightIndent=20,
        spaceAfter=10
    )

    caption_style = ParagraphStyle(
        'CustomCaption',
        parent=styles['Normal'],
        fontSize=10,
        alignment=1,
        textColor=colors.darkgrey,
        spaceAfter=20,
        fontName='Helvetica-Oblique'
    )

    # Build PDF content
    story = []

    # Add logo at the top
    if os.path.exists('nyc_taxi_logo.png'):
        logo = Image('nyc_taxi_logo.png', width=2*inch, height=1.5*inch)
        logo.hAlign = 'CENTER'
        story.append(logo)
        story.append(Spacer(1, 20))

    # Add title
    story.append(Paragraph("NYC Taxi Data Enrichment Pipeline", title_style))
    story.append(Paragraph("Advanced Feature Engineering for Urban Transportation Analytics", subtitle_style))
    story.append(Spacer(1, 30))

    current_section = ""
    figure_counter = 1

    for section in sections:
        section = section.strip()
        if not section:
            continue
        section = section.strip()
        if not section:
            continue

        # Title detection
        if section.startswith('# '):
            title = section[2:].strip()
            story.append(Paragraph(title, title_style))
            story.append(Spacer(1, 20))

        # Heading 2 detection - check for section names instead of markdown syntax
        elif 'Visualization and Analysis' in section or 'Results and Analysis' in section:
            if 'Visualization and Analysis' in section:
                heading = 'Visualization and Analysis'
                current_section = 'visualization_and_analysis'
            elif 'Results and Analysis' in section:
                heading = 'Results and Analysis'
                current_section = 'results_and_analysis'

            story.append(Paragraph(heading, heading2_style))
            story.append(Spacer(1, 15))

            # Add charts after specific sections
            if 'visualization' in current_section:
                charts_story = add_visualization_charts(figure_counter, caption_style)
                story.extend(charts_story)
                figure_counter += 5
            elif 'results' in current_section:
                charts_story = add_visualization_charts(figure_counter, caption_style)
                story.extend(charts_story)
                figure_counter += 5

        # Heading 3 detection - check for subsection names
        elif 'Data Source and Preprocessing' in section or 'Feature Engineering Implementation' in section or 'Data Validation Framework' in section:
            if 'Data Source and Preprocessing' in section:
                subheading = 'Data Source and Preprocessing'
            elif 'Feature Engineering Implementation' in section:
                subheading = 'Feature Engineering Implementation'
            elif 'Data Validation Framework' in section:
                subheading = 'Data Validation Framework'
            story.append(Paragraph(subheading, heading3_style))
            story.append(Spacer(1, 10))

        # Code blocks
        elif section.startswith('```') or '    ' in section or section.count('`') >= 2:
            if section.startswith('```'):
                code_content = section.replace('```', '').strip()
            else:
                code_content = section.replace('    ', '').strip()
            story.append(Paragraph(code_content, code_style))
            story.append(Spacer(1, 10))

        # Lists
        elif section.startswith('- ') or section.startswith('* '):
            list_items = section.split('\n')
            for item in list_items:
                if item.strip().startswith(('- ', '* ')):
                    list_text = item.strip()[2:]
                    story.append(Paragraph(f"• {list_text}", normal_style))

        # Regular paragraphs
        else:
            if len(section) > 50:  # Longer text
                story.append(Paragraph(section, normal_style))
                story.append(Spacer(1, 10))

    # Add signature page
    story.append(PageBreak())
    story.append(Paragraph("Author Information", title_style))
    story.append(Spacer(1, 30))

    signature_info = f"""
    <b>Author:</b> {author_name}<br/>
    <b>Date:</b> September 15, 2025<br/>
    <b>Project:</b> NYC Taxi Data Enrichment Pipeline<br/>
    <b>Description:</b> Advanced feature engineering for urban transportation analytics<br/>
    <br/>
    <i>This article demonstrates sophisticated data enrichment techniques applied to NYC yellow taxi data, including velocity analysis, tipping behavior patterns, trip classification, and temporal analytics.</i>
    """

    story.append(Paragraph(signature_info, normal_style))

    # Generate PDF
    doc.build(story)

    print(f"PDF generated successfully: {output_pdf_file}")
    print(f"Author: {author_name}")
    print(f"Pages: Generated with logo and charts")

def add_visualization_charts(start_figure, caption_style):
    """Add visualization charts to the PDF"""
    story = []

    # Check if plots directory exists
    if not os.path.exists('plots'):
        return story

    charts = [
        ('plots/nyc_taxi_features_overview.png', f'Figure {start_figure}: Overview dashboard showing all new features including trip speed distribution, tip percentage analysis, trip type classification, and peak hour indicators.'),
        ('plots/speed_vs_distance.png', f'Figure {start_figure + 1}: Scatter plot analysis of trip speed versus distance, revealing velocity patterns and correlations in taxi transportation.'),
        ('plots/tip_by_trip_type.png', f'Figure {start_figure + 2}: Box plot comparison of tip percentages across different trip types (short, medium, long), showing behavioral patterns.'),
        ('plots/speed_by_peak_hour.png', f'Figure {start_figure + 3}: Comparative analysis of speed distributions between peak and off-peak hours, highlighting traffic impact.'),
        ('plots/correlation_matrix.png', f'Figure {start_figure + 4}: Correlation matrix heatmap showing relationships between all new features and their interdependencies.')
    ]

    for chart_path, caption in charts:
        if os.path.exists(chart_path):
            try:
                # Add chart
                chart = Image(chart_path, width=6*inch, height=4*inch)
                chart.hAlign = 'CENTER'
                story.append(chart)
                story.append(Spacer(1, 10))

                # Add caption
                story.append(Paragraph(caption, caption_style))
                story.append(Spacer(1, 20))
            except Exception as e:
                pass
        else:
            pass

    return story

if __name__ == "__main__":
    input_file = "NYC_TAXI_FEATURE_ENGINEERING_ARTICLE.md"
    output_file = "NYC_Taxi_Feature_Engineering_Article_Pedro_Musculini.pdf"

    if os.path.exists(input_file):
        markdown_to_pdf_with_signature(input_file, output_file, "Pedro Musculini")
    else:
        print(f"Error: {input_file} not found!")