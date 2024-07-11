import React from 'react';
import { useFormik } from 'formik';

const CreateEvent = () => {
    const formik = useFormik({
        initialValues: {
            eventName: '',
            date: '',
            location: '',
        },
        onSubmit: values => {
            alert(JSON.stringify(values, null, 2));
        },
    });

    return (
        <form onSubmit={formik.handleSubmit}>
            <label htmlFor="eventName">Event Name</label>
            <input
                id="eventName"
                name="eventName"
                type="text"
                onChange={formik.handleChange}
                value={formik.values.eventName}
            />
            <br />
            <label htmlFor="date">Date</label>
            <input
                id="date"
                name="date"
                type="date"
                onChange={formik.handleChange}
                value={formik.values.date}
            />
            <br />
            <label htmlFor="location">Location</label>
            <input
                id="location"
                name="location"
                type="text"
                onChange={formik.handleChange}
                value={formik.values.location}
            />
            <br />
            <button type="submit">Create Event</button>
        </form>
    );
};

export default CreateEvent;
