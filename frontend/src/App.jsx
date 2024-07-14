
import { Routes, Route } from 'react-router-dom';
import Homepage from './Home';
import Events from './Events';
import CreateEvent from './CreateEvent'
import NavBar from './NavBar';


function App() {
  return (
    
      <Routes>
       
       
        <Route path="/" element={<Homepage />} />
        <Route path="/navbar" element={<NavBar/>} />

        
        <Route path="/events" element={<Events />} />

        <Route path="/createevent" element={<CreateEvent />} />
       
        
      </Routes>
    
  );
}

export default App;
