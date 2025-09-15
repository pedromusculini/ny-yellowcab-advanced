# NYC Taxi Data Enrichment Pipeline

This project enhances the## PDF Version

A professionally formatted PDF version of the article is also available:

📕 **[NYC Taxi Feature Engineering Article (PDF)](NYC_Taxi_Feature_Engineering_Article_Pedro_Musculini.pdf)**

**Author:** Pedro Musculini  
**Date:** September 15, 2025

The PDF includes:
- ✅ **Professional logo** at the top
- ✅ **Academic formatting** with proper styling
- ✅ **All 5 visualization charts** with detailed captions
- ✅ **Author signature** and publication information
- ✅ **Print-ready layout** optimized for sharing

**Charts Included:**
- Figure 1: Overview dashboard with all new features
- Figure 2: Speed vs Distance scatter plot analysis
- Figure 3: Tip percentage by trip type comparison
- Figure 4: Peak hour speed distribution comparison
- Figure 5: Feature correlation matrix heatmap

### Generating PDF
```bash
python scripts/markdown_to_pdf.py
```line for NYC yellow taxi data by adding new derived features to enrich the analysis.

## Project Logo

![NYC Taxi Analytics Logo](nyc_taxi_logo.png)

### Logo Creation Process

The project logo was created using automated Python scripting with matplotlib:

#### Design Elements
- **Color Scheme**: Professional blue gradient (#1e3a8a to #3b82f6)
- **Typography**: Clean, modern sans-serif fonts
- **Icon Elements**: Taxi silhouette with data visualization motifs
- **Layout**: Balanced composition with text and graphic elements

#### Technical Implementation
- **Library**: Matplotlib for vector graphics generation
- **Formats**: Both PNG (raster) and SVG (vector) outputs
- **Resolution**: High-DPI for professional quality
- **Scalability**: Vector format supports any size without quality loss

#### Generation Script
```bash
python scripts/create_logo.py
```

**Output Files**:
- `nyc_taxi_logo.png`: Raster format (300 DPI)
- `nyc_taxi_logo.svg`: Vector format (scalable)

## New Features

### Trip Speed (`trip_speed_mph`)
- Calculated as `trip_distance / (trip_duration / 3600)` (miles per hour).
- Capped at a maximum of 100 mph to avoid unrealistic values.

### Tip Percentage (`tip_percentage`)
- Calculated as `(tip_amount / total_amount) * 100`.
- NaN values filled with 0, capped at a maximum of 100%.

### Trip Type (`trip_type`)
- Categorized as "short" (< 10 min), "medium" (10-30 min), or "long" (> 30 min) based on duration.

### Peak Hour Indicator (`is_peak_hour`)
- 1 if pickup hour is between 7-9 AM or 5-7 PM, otherwise 0.

## Installation & Setup

### Prerequisites
- Python 3.11 or higher
- pip package manager
- Git (for cloning the repository)

### Quick Start
```bash
# Clone the repository
git clone https://github.com/pedro-musculini/nyc-taxi-pipeline.git
cd nyc-taxi-pipeline

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Alternative: Install as package
pip install -e .
```

### Development Setup
```bash
# Install development dependencies
pip install -r requirements.txt
pip install -e ".[dev]"

# Run tests
pytest

# Format code
black scripts/
isort scripts/

# Type checking
mypy scripts/
```

### Data Setup
1. Create a `data/` directory in the project root
2. Place your NYC taxi data file as `data/nyc_taxi_raw.csv`
3. The data should contain columns: `pickup_datetime`, `dropoff_datetime`, `trip_distance`, `fare_amount`, `tip_amount`, etc.

## Data Visualization

The project includes comprehensive visualizations for the new features:

### Generated Plots
- **nyc_taxi_features_overview.png**: Overview dashboard with all new features
- **speed_vs_distance.png**: Scatter plot of trip speed vs distance
- **tip_by_trip_type.png**: Box plot of tip percentages by trip type
- **speed_by_peak_hour.png**: Speed distribution comparison between peak and off-peak hours
- **correlation_matrix.png**: Correlation heatmap of all new features

### Running Visualizations
```bash
python scripts/visualize_data.py
# or
make visualize
```

## Technical Article

A comprehensive technical article about this project is available:

📄 **[NYC Taxi Feature Engineering Article](NYC_TAXI_FEATURE_ENGINEERING_ARTICLE.md)**

The article covers:
- Advanced feature engineering techniques
- Data validation methodologies
- Visualization strategies
- Performance analysis
- Implementation details
- Future research directions

### Article Creation Process

The technical article was created through a systematic approach combining automated content generation and manual refinement:

#### Content Generation Tools
- **Python Markdown Library**: For text formatting and structure
- **ReportLab**: Professional PDF generation with embedded graphics
- **Matplotlib/Seaborn**: High-quality visualization creation
- **Custom Logo Generation**: Automated logo creation using matplotlib

#### Article Structure
- **Abstract**: Project overview and objectives
- **Introduction**: Background and motivation
- **Methodology**: Technical implementation details
- **Feature Engineering**: Detailed explanation of each derived feature
- **Data Validation**: Quality assurance methodologies
- **Visualization & Analysis**: Graphical analysis techniques
- **Results**: Performance metrics and insights
- **Implementation Details**: Technical stack and architecture
- **Conclusion**: Summary and future directions

#### Automated Features
- **Dynamic Chart Integration**: All 5 visualization charts automatically embedded
- **Professional Logo**: Custom-generated project branding
- **Author Attribution**: Automated signature and publication information
- **Academic Formatting**: Professional styling with proper typography

### PDF Generation Pipeline

The PDF version was created using a custom Python script with the following components:

#### Core Technologies
- **ReportLab PDF Library**: Professional document generation
- **Markdown Processing**: Text-to-PDF conversion with formatting preservation
- **Image Integration**: Automatic embedding of charts and logos
- **Typography System**: Custom fonts and styling for academic presentation

#### PDF Features
- **Multi-page Layout**: Automatic page breaks and flow management
- **High-Resolution Graphics**: All charts embedded at 300 DPI
- **Professional Styling**: Academic formatting with consistent typography
- **Print Optimization**: Optimized for both digital viewing and printing
- **Metadata Integration**: Author information and publication details

#### Generation Command
```bash
python scripts/markdown_to_pdf.py
```

**Output**: `NYC_Taxi_Feature_Engineering_Article_Pedro_Musculini.pdf` (818 KB)

## PDF Version

A professionally formatted PDF version of the article is also available:

📕 **[NYC Taxi Feature Engineering Article (PDF)](NYC_Taxi_Feature_Engineering_Article_Pedro_Musculini.pdf)**

**Author:** Pedro Musculini  
**Publication Date:** September 15, 2025

### PDF Generation Details

The PDF was created using a sophisticated pipeline that combines multiple technologies:

#### Development Tools & Libraries
- **Python 3.11+**: Core programming language
- **ReportLab 4.0+**: Professional PDF generation library
- **Markdown Library**: Text processing and HTML conversion
- **Matplotlib**: Chart generation and logo creation
- **Pillow (PIL)**: Image processing and optimization

#### PDF Features
- ✅ **Professional logo** at the top (custom-generated)
- ✅ **Academic formatting** with proper styling and typography
- ✅ **All 5 visualization charts** with detailed captions
- ✅ **Author signature** and publication information
- ✅ **Print-ready layout** optimized for sharing
- ✅ **High-resolution graphics** (300 DPI)
- ✅ **Automatic page breaks** and flow management
- ✅ **Metadata integration** with author and publication details

#### Embedded Charts
1. **Figure 1**: Overview dashboard with all new features
2. **Figure 2**: Speed vs Distance scatter plot analysis
3. **Figure 3**: Tip percentage by trip type comparison
4. **Figure 4**: Peak hour speed distribution comparison
5. **Figure 5**: Feature correlation matrix heatmap

### Technical Implementation

The PDF generation script (`scripts/markdown_to_pdf.py`) implements:

#### Key Components
- **Section Detection**: Automatic identification of article sections
- **Chart Integration**: Dynamic embedding of visualization graphics
- **Typography System**: Custom paragraph styles for different content types
- **Layout Management**: Professional spacing and alignment
- **Error Handling**: Robust processing with fallback mechanisms

#### Processing Pipeline
1. **Markdown Parsing**: Convert MD to HTML structure
2. **Content Extraction**: Clean text and identify sections
3. **Visual Asset Integration**: Embed logo and charts
4. **PDF Assembly**: Build final document with professional formatting
5. **Metadata Addition**: Include author and publication information

### Generating PDF
```bash
python scripts/markdown_to_pdf.py
```

**Output File**: `NYC_Taxi_Feature_Engineering_Article_Pedro_Musculini.pdf`  
**File Size**: ~818 KB (includes all graphics and professional formatting)

## Files

### Core Scripts
- `scripts/clean_curate.py`: Main script for cleaning and feature derivation
- `scripts/validate_curated.py`: Validation of enriched data quality
- `scripts/visualize_data.py`: Data visualization and plotting generation
- `scripts/create_logo.py`: Automated logo generation script
- `scripts/markdown_to_pdf.py`: Professional PDF generation with embedded graphics

### Test Files
- `tests/test_validate_curated.py`: Unit tests for data validation

### Documentation
- `README.md`: Project documentation and usage guide
- `CONTRIBUTING.md`: Guidelines for contributors
- `NYC_TAXI_FEATURE_ENGINEERING_ARTICLE.md`: Technical article in Markdown format
- `LICENSE`: MIT license file

### Generated Assets
- `NYC_Taxi_Feature_Engineering_Article_Pedro_Musculini.pdf`: Professional PDF article
- `nyc_taxi_logo.png`: Project logo (PNG format, 300 DPI)
- `nyc_taxi_logo.svg`: Project logo (SVG vector format)
- `plots/`: Directory containing all generated visualization charts

### Configuration Files
- `requirements.txt`: Python dependencies specification
- `setup.py`: Package installation configuration
- `pyproject.toml`: Modern Python project configuration
- `Makefile`: Task automation for common operations
- `.gitignore`: Git ignore patterns for Python projects

### Data Directory
- `data/`: Directory for input data files (not included in repository)

## Project Status

### Current Version: 1.0.0
- ✅ Core feature engineering pipeline complete
- ✅ Data validation framework implemented
- ✅ Comprehensive visualization suite
- ✅ Professional documentation and PDF generation
- ✅ Automated logo generation
- ✅ Unit testing coverage
- ✅ MIT license and contribution guidelines

### Recent Updates
- **v1.0.0** (September 15, 2025): Complete pipeline with professional documentation
  - Added automated PDF generation with embedded charts
  - Created professional project logo
  - Enhanced README with detailed technical documentation
  - Added comprehensive requirements.txt and setup.py
  - Implemented MIT license and contribution guidelines

## Roadmap

### Short Term (Next Release)
- [ ] Performance optimizations for large datasets
- [ ] Additional visualization types (geospatial maps)
- [ ] Enhanced data validation rules
- [ ] API development for real-time processing

### Medium Term
- [ ] Machine learning integration for predictive analytics
- [ ] Web interface for interactive exploration
- [ ] Multi-format data export capabilities
- [ ] Cloud deployment options (AWS, GCP)

### Long Term
- [ ] Real-time data streaming pipeline
- [ ] Advanced ML models for demand prediction
- [ ] Multi-city expansion capabilities
- [ ] Integration with transportation APIs

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details on:
- Development setup and workflow
- Code style guidelines
- Testing requirements
- Pull request process

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Citation

If you use this project in your research or work, please cite:

```bibtex
@software{musculini_nyc_taxi_pipeline_2025,
  author = {Musculini, Pedro},
  title = {NYC Taxi Data Enrichment Pipeline},
  year = {2025},
  url = {https://github.com/pedro-musculini/nyc-taxi-pipeline},
  version = {1.0.0}
}
```

## Acknowledgments

- **NYC Taxi and Limousine Commission (TLC)**: For providing the comprehensive taxi dataset
- **Python Data Science Community**: For the excellent libraries and tools
- **Open Source Contributors**: For making this project possible

---

**Author**: Pedro Musculini  
**Contact**: [Your contact information]  
**Project**: NYC Taxi Data Enrichment Pipeline  
**Date**: September 15, 2025