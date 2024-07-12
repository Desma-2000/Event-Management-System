import  { useEffect, useState } from 'react';
import Register from './Register';


function Events() {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    fetch('/events')
      .then((response) => response.json())
      .then((data) => setEvents(data));
  }, []);

  return (
    <div>
      <h2>Events</h2>
      <ul>
        {events.map((event) => (
          <li key={event.id}>
            <h3>{event.title}</h3>
            <p>{event.description}</p>
            <p>{new Date(event.date).toLocaleDateString()}</p>
            <p>{event.location}</p>
            <Register eventId={event.id} />
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Events;
