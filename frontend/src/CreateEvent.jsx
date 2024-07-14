
import  { useState } from 'react';
import { Formik, Form, Field, ErrorMessage } from 'formik';
import { useNavigate } from 'react-router-dom';
import './CreateEvent.css';

const CreateEvent = () => {
  const navigate = useNavigate();
  const [showSuccessMessage, setShowSuccessMessage] = useState(false);

  // Example function to check authentication status (replace with your actual logic)
  const isLoggedIn = () => {
    // Check if user is logged in (e.g., check for JWT token in local storage)
    return localStorage.getItem('accessToken') !== null; // Adjust as per your authentication logic
  };

  const handleSubmit = async (values, { setSubmitting }) => {
    try {
      // Check if user is authenticated
      if (!isLoggedIn()) {
        // Redirect to login page if not authenticated
        navigate('/login');
        return;
      }

      // Simulate success
      setShowSuccessMessage(true);

      // Redirect to events page after successful creation
      setTimeout(() => {
        navigate('/events');
      }, 2000); // Redirect after 2 seconds

    } catch (error) {
      console.error('Error creating event:', error);
    } finally {
      setSubmitting(false); // Reset form submission state
    }
  };

  const handleEditEvent = () => {
    // Redirect to edit event page or implement edit functionality here
    navigate('/edit-event'); // Example redirection
  };

  const handleDeleteEvent = async () => {
    try {
      // Implement delete event functionality
      // Example: Make a DELETE request to the API endpoint to delete the event

      // Simulate success
      alert('Event deleted successfully');
      navigate('/events'); // Redirect to events page after deletion
    } catch (error) {
      console.error('Error deleting event:', error);
      // Handle error gracefully
    }
  };

  return (
    <div className="create-event-container">
      <h2>Create Event</h2>
      <div className="create-event-form">
        <Formik initialValues={{ 'Event Name': '', 'Date': '', 'Location': '' }} onSubmit={handleSubmit}>
          {({ isSubmitting }) => (
            <Form>
              <div className="form-group">
                <label htmlFor="Event Name">Event Name:</label>
                <Field type="text" id="Event Name" name="Event Name" />
                <ErrorMessage name="Event Name" component="div" />
              </div>

              <div className="form-group">
                <label htmlFor="Date">Date:</label>
                <Field type="date" id="Date" name="Date" />
                <ErrorMessage name="Date" component="div" />
              </div>

              <div className="form-group">
                <label htmlFor="Location">Location:</label>
                <Field type="text" id="Location" name="Location" />
                <ErrorMessage name="Location" component="div" />
              </div>

              <div className="form-buttons">
                <button type="submit" disabled={isSubmitting}>
                  Create Event
                </button>

                {/* Edit and Delete Buttons */}
                <div className="edit-delete-buttons">
                  <button type="button" onClick={handleEditEvent}>
                    Edit Event
                  </button>
                  <button type="button" onClick={handleDeleteEvent}>
                    Delete Event
                  </button>
                </div>
              </div>
            </Form>
          )}
        </Formik>

        {showSuccessMessage && (
          <p className="success-message">Event created successfully! Redirecting...</p>
        )}
      </div>
    </div>
  );
};

export default CreateEvent;