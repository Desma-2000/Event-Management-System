
import PropTypes from 'prop-types';

function Register({ eventId }) {
  const handleRegister = () => {
    // Registration logic here
    console.log('Register for event:', eventId);
  };

  return (
    <button onClick={handleRegister}>Register</button>
  );
}

Register.propTypes = {
  eventId: PropTypes.number.isRequired,
};

export default Register;
