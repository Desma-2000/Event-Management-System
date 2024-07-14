
import { useNavigate, Link } from 'react-router-dom';
import './Home.css'
import Events from './Events';


function Homepage() {
  
  const navigate = useNavigate();

  const handleCreateEvent = () => {
    navigate('/createevent');
  };

  return (
    <div className="homepage-container">
      <h1>Welcome to Event Management System</h1>
      <div>
        <nav>
        <ul className="nav-menu">
        <li><Link to="/homepage">HomePage</Link></li>
        <li><Link to="/signup">Signup</Link></li>
        <li><Link to="/login">Login</Link></li>
        <li><Link to="/events">events</Link></li>
        </ul>
        </nav>
      </div>
      <div className = 'display-events'>
        <Events/>
      </div>
      <div className = 'create-events-button'>
        <button onClick={handleCreateEvent}>Create Event</button>
      </div>
    </div>
  );
}

export default Homepage;
