import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import CreateEvent from './components/CreateEvent';
import './App.css';

function App() {
    return (
        <Router>
            <div className="App">
                <nav>
                    <ul>
                        <li>
                            <Link to="/">Home</Link>
                        </li>
                        <li>
                            <Link to="/create-event">Create Event</Link>
                        </li>
                    </ul>
                </nav>

                <Routes>
                    <Route path="/create-event" element={<CreateEvent />} />
                    <Route path="/" element={<h2>Welcome to the Event Management System</h2>} />
                </Routes>
            </div>
        </Router>
    );
}

export default App;
