# GS AI - Ecommerce Chatbot Interface

A React-based frontend for an ecommerce chatbot interface built without Node.js dependencies. This project uses CDN links for React and other libraries, making it easy to run directly in a browser.

## Features

- **Authentication**: Sign up/Sign in functionality
- **Chat Interface**: Real-time chat with AI assistant
- **Camera Integration**: Visual product search with image capture/upload
- **Settings Page**: User preferences and account management
- **Feedback System**: User feedback collection with ratings
- **Dark Theme**: Modern black-themed UI with GS AI branding
- **Responsive Design**: Works on desktop and mobile devices

## Setup Instructions

1. **Download/Clone the project files**
2. **Open `index.html` in your web browser**
3. **That's it! No installation required**

## File Structure

\`\`\`
gs-ai-ecommerce-chatbot/
├── index.html              # Main HTML file
├── styles.css              # All CSS styles
├── components/
│   ├── Avatar.js           # Avatar component
│   ├── Button.js           # Button and form components
│   ├── Input.js            # Input, Select, Switch components
│   ├── Card.js             # Card components
│   ├── Toast.js            # Toast notification system
│   ├── AuthPage.js         # Authentication page
│   ├── Sidebar.js          # Navigation sidebar
│   ├── ChatInterface.js    # Main chat interface
│   ├── SettingsPage.js     # Settings page
│   ├── FeedbackPage.js     # Feedback page
│   └── CameraPage.js       # Camera/visual search page
├── App.js                  # Main application component
└── README.md               # This file
\`\`\`

## Usage

### Authentication
- Use any email/password combination to sign in (demo mode)
- Sign up creates a new account (demo mode)

### Chat Interface
- Type messages to interact with the AI assistant
- AI provides ecommerce-related responses
- Messages are displayed in real-time with typing indicators

### Camera Feature
- Click "Start Camera" to use device camera
- Upload images for product analysis
- AI analyzes images and provides product information

### Settings
- Update profile information
- Configure notifications
- Change language preferences
- Manage privacy settings

### Feedback
- Submit different types of feedback
- Rate your experience
- View previously submitted feedback

## Customization

### Connecting to Backend
To connect this frontend to your FastAPI backend:

1. **Update API calls** in the chat interface
2. **Replace mock responses** with real API calls
3. **Add authentication** integration
4. **Implement real image analysis** for camera feature

### Styling
- Modify `styles.css` for custom styling
- Update CSS variables for color scheme changes
- Add new components following the existing pattern

### Adding Features
- Create new component files in the `components/` folder
- Add navigation items in `Sidebar.js`
- Update the routing logic in `App.js`

## Browser Compatibility

This application works in modern browsers that support:
- ES6+ JavaScript features
- CSS Grid and Flexbox
- Camera API (for camera features)
- Local Storage

## Development Notes

- Uses React 18 via CDN
- Babel standalone for JSX compilation
- Font Awesome for icons
- No build process required
- All dependencies loaded via CDN

## Integration with Backend

When ready to integrate with your FastAPI + LLM + SQL backend:

1. Replace the mock `generateAIResponse` function with real API calls
2. Add proper authentication endpoints
3. Implement real product search and analysis
4. Connect to your database for user management
5. Add environment variables for API keys

## License

This project is created for educational/demonstration purposes.
