import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Login from './Login';
import Logout from './Logout';
import Register from './Register'; // Import Register component
// Import other components as needed

function App() {
    return (
        <Router>
            <Routes>
                <Route path="/login" element={<Login />} />
                <Route path="/logout" element={<Logout />} />
                <Route path="/register" element={<Register />} /> {/* Add Register route */}
                {/* Add other routes here */}
            </Routes>
        </Router>
    );
}

export default App;
