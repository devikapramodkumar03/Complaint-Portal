# Citizen Connect  
### Transparent Civic Complaint Management Platform

Citizen Connect is a web-based civic engagement platform that bridges the gap between citizens and government officials through transparent complaint management and real-time progress tracking.

This repository contains a fully functional Flask-based web application that enables citizens to report local issues while allowing government officials to efficiently manage and resolve complaints with full transparency and community-driven prioritization.

---

## Core Features

### For Citizens
- Submit complaints with photos and geolocation tagging
- View neighborhood complaints in a social media-style scrollable feed
- Upvote/downvote community issues to prioritize and filter relevant complaints
- Track real-time progress of complaint resolution through visual progress bars
- Filter complaints by status (All, Most Upvoted, Recent, In Progress)
- Access helpline numbers and public notices

### For Government Officials
- Comprehensive dashboard with complaint overview and statistics
- Real-time analytics showing total, under review, in progress, and completed complaints
- Three-stage progress update system (Review → In Progress → Completed)
- Advanced filtering by status and location-based search
- Add resolution notes for transparency
- Performance metrics and efficiency tracking visible to all users

---

## Problem Statement

Citizens often face challenges when reporting civic issues such as potholes, broken streetlights, water supply problems, and sanitation concerns. Traditional complaint systems lack:
- Transparency in resolution progress
- Community-driven prioritization
- Real-time status updates
- Direct communication between citizens and officials
- Performance accountability

Citizen Connect addresses these gaps by providing a transparent, democratic platform where community concerns are visible, prioritized through voting, and tracked until resolution.

---

## Key Innovation

### Community-Driven Filtering
Citizens play an active role in the complaint resolution process through a voting mechanism:
- **Upvote** important and legitimate complaints to increase their priority
- **Downvote** irrelevant or duplicate complaints to filter them out
- High upvote counts signal urgency and community consensus to government officials
- Democratic prioritization ensures the most pressing issues receive immediate attention

### Government Performance Transparency
- **Real-time Statistics**: Public dashboard displays total complaints, pending reviews, active resolutions, and completed issues
- **Progress Tracking**: Visual progress bars show exact status of each complaint (Review → In Progress → Completed)
- **Efficiency Metrics**: Resolution rates and response times are visible to all users
- **Accountability**: Timestamp tracking and resolution notes create an audit trail
- **Performance Indicators**: Officials' resolution statistics demonstrate responsiveness and effectiveness

This dual mechanism empowers citizens while holding government officials accountable through transparent performance metrics.

---

## Technical Stack

**Frontend:** HTML5, CSS3, JavaScript (Vanilla)  
**Backend:** Flask (Python)  
**Database:** SQLite (Development) / MongoDB Atlas (Production)  
**Hosting:** Render Cloud Platform  
**File Storage:** Local storage with cloud migration support

---

## Installation & Setup

**Prerequisites:**  
Python 3.7 or higher

**Steps:**
```bash
# Clone repository
git clone https://github.com/yourusername/citizen-connect.git
cd citizen-connect

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run application
python app.py

# Access at http://localhost:5000
```

---

## Test Credentials

**Citizen Account:**  
Email: `priyasharma@gmail.com`  
Password: `password123`

**Government Official Account:**  
Email: `govtofficial@gmail.com`  
Password: `official123`

---

## Key Technical Implementation

### Progress Tracking System
Three-stage workflow with visual indicators:
- **Review** (25% - Orange): Initial assessment and validation
- **In Progress** (65% - Blue): Active resolution work
- **Completed** (100% - Green): Issue resolved and verified

### Voting & Prioritization
Democratic system where citizens upvote important issues and downvote irrelevant ones. High upvote counts increase visibility and urgency for government officials. Vote tracking prevents duplicate voting and ensures fair prioritization.

### Real-time Updates
AJAX-based status updates allow officials to change complaint progress without page reloads. Changes are immediately reflected in the citizen feed with animated progress bar transitions.

### Geolocation Integration
Browser Geolocation API automatically tags complaint location with latitude/longitude coordinates and converts them to readable addresses for easy identification.

### Performance Analytics
Dashboard displays real-time statistics including:
- Total complaints received
- Complaints under review
- Active resolutions in progress
- Successfully completed issues
- Average resolution time
- Government efficiency rate

---

## Database Schema

**Users:** Stores citizen and official accounts with role-based access  
**Complaints:** Contains complaint details, photos, location, status, and votes  
**Votes:** Tracks user voting to prevent duplicates  
**Status History:** Maintains audit trail of all progress updates

---

## Future Enhancements

- Email/SMS notifications for status updates
- Mobile application (Android/iOS)
- AI-powered complaint categorization
- Multi-language support (Hindi, regional languages)
- Before/after photo verification system
- Community discussion threads
- Advanced analytics dashboard with trend analysis
- Integration with government department APIs
- Predictive analytics for recurring issues

---

## Project Status

**Current Version:** 1.0  
Fully Functional Web Application – Deployed and Ready for Use
