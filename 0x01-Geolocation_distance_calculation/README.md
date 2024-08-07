# Geolocation Distance Calculation

This project calculates the distance between two locations given their postal codes using the OpenCage Geocoder API and the Haversine formula.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Contributing](#contributing)
- [Contact](#contact)

## Introduction

The Geolocation Distance Calculation script retrieves geographical coordinates for given postal codes and calculates the distance between these locations. This is useful for various applications such as logistics, travel, and geographic data analysis.

## Features

- Retrieve geographical coordinates using the OpenCage Geocoder API.
- Calculate distance between two locations using the Haversine formula.
- Simple and easy-to-use Python script.

## Tech Stack

- Python
- OpenCage Geocoder API

## Installation

1. Clone the repository:

```bash
git clone https://github.com/nyvnge/geolocation-distance-calculation.git
```

2. Navigate to the project directory:

```bash
cd geolocation-distance-calculation
```

3. Install the required Python packages:

```bash
pip install requests
```

## Usage

1. Replace the `API_KEY` variable in the script with your own OpenCage Geocoder API key:

```python
API_KEY = 'your_api_key_here'
```

2. Run the script:

```bash
python geolocation_distance_calculation.py
```

3. Enter the postal codes when prompted:

```bash
Enter the first postcode: 12345
Enter the second postcode: 67890
```

4. The script will output the distance between the two postal codes:

```bash
The distance between 12345 and 67890 is X.XX kilometers.
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## Contact

Sanderson Mwakamba Nyange  
Email: sandersonnyange@gmail.com  
LinkedIn: [Sanderson Nyange](https://www.linkedin.com/in/sanderson-nyange-7a6a10238/)  
GitHub: [nyvnge](https://www.github.com/nyvnge/)

---
