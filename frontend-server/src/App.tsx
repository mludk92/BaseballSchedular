import { useState, useEffect } from 'react';
import './App.css';

interface Event {
  id: number;
  date: string; // YYYY-MM-DD
  time: string;
  place: string;
  note: string;
}

function getDaysInMonth(year: number, month: number) {
  return new Date(year, month + 1, 0).getDate();
}

function App() {
  const [events, setEvents] = useState<Event[]>([]);
  const [selectedDate, setSelectedDate] = useState<string | null>(null);
  const [modalOpen, setModalOpen] = useState(false);
  const [form, setForm] = useState<{ time: string; place: string; note: string }>({
    time: '',
    place: '',
    note: '',
  });
  const [editId, setEditId] = useState<number | null>(null);


  // Backend API URL
  const API_URL = 'http://127.0.0.1:8000/events/';

  // Fetch events from backend on mount
  useEffect(() => {
    fetch(API_URL)
      .then(res => res.json())
      .then(data => setEvents(data))
      .catch(() => setEvents([]));
  }, []);

  // Calendar setup
  const today = new Date();
  const year = today.getFullYear();
  const month = today.getMonth();
  const daysInMonth = getDaysInMonth(year, month);
  const dayLabels = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
  const firstDayOfWeek = new Date(year, month, 1).getDay();

  // Open modal to add/edit event
  const openModal = (date: string, event?: Event) => {
    setSelectedDate(date);
    setModalOpen(true);
    if (event) {
      setForm({ time: event.time, place: event.place, note: event.note });
      setEditId(event.id);
    } else {
      setForm({ time: '', place: '', note: '' });
      setEditId(null);
    }
  };


  // Save new or edited event (API integration)
  const saveEvent = async () => {
    if (!selectedDate) return;
    const payload = {
      date: selectedDate,
      time: form.time,
      place: form.place,
      note: form.note,
    };
    if (editId !== null) {
      // Edit
      await fetch(`${API_URL}${editId}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
      });
    } else {
      // Add
      await fetch(API_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
      });
    }
    // Refresh events
    fetch(API_URL)
      .then(res => res.json())
      .then(data => setEvents(data));
    setModalOpen(false);
    setForm({ time: '', place: '', note: '' });
    setEditId(null);
  };


  // Delete event (API integration)
  const deleteEvent = async (id: number) => {
    await fetch(`${API_URL}${id}`, { method: 'DELETE' });
    // Refresh events
    fetch(API_URL)
      .then(res => res.json())
      .then(data => setEvents(data));
    setModalOpen(false);
  };

  // Get events for a specific date
  const eventsForDate = (date: string) =>
    events.filter(ev => ev.date === date);

  // Render calendar grid with blanks for days before the 1st
  const calendarSquares = [];
  for (let i = 0; i < firstDayOfWeek; i++) {
    calendarSquares.push(<div key={`blank-${i}`} className="calendar-square blank"></div>);
  }
  for (let day = 1; day <= daysInMonth; day++) {
    const dateStr = `${year}-${String(month + 1).padStart(2, '0')}-${String(day).padStart(2, '0')}`;
    calendarSquares.push(
      <div
        key={dateStr}
        className="calendar-square"
        onClick={() => openModal(dateStr)}
      >
        <div className="calendar-day">{day}</div>
        <div className="calendar-events">
          {eventsForDate(dateStr).map(ev => (
            <div
              key={ev.id}
              className="event"
              onClick={e => {
                e.stopPropagation();
                openModal(dateStr, ev);
              }}
            >
              <span className="event-time-place">{ev.time} - {ev.place}</span>
              {ev.note && (
                <span className="event-note"> &nbsp;|&nbsp; {ev.note}</span>
              )}
            </div>
          ))}
        </div>
      </div>
    );
  }

  return (
    <div className="calendar-container">
      <header className="main-header">
        <h1>Baseball Scheduling</h1>
        <p className="subtitle">Organize your games and events with ease!</p>
      </header>
      <h2 className="month-title">
        {today.toLocaleString('default', { month: 'long' })} {year}
      </h2>
      <div className="calendar-day-labels">
        {dayLabels.map(label => (
          <div key={label}>{label}</div>
        ))}
      </div>
      <div className="calendar-grid">{calendarSquares}</div>

      {/* Modal for adding/editing events */}
      {modalOpen && (
        <div className="modal">
          <div className="modal-content">
            <h3>
              {editId ? 'Edit Event' : 'Add Event'} for {selectedDate}
            </h3>
            <form className="event-form-modal" onSubmit={e => { e.preventDefault(); saveEvent(); }}>
              <div className="event-form-row">
                <div className="event-form-group">
                  <label htmlFor="event-time">Time:</label>
                  <input
                    id="event-time"
                    type="time"
                    value={form.time}
                    onChange={e => setForm({ ...form, time: e.target.value })}
                    required
                  />
                </div>
                <div className="event-form-group">
                  <label htmlFor="event-place">Place:</label>
                  <input
                    id="event-place"
                    type="text"
                    value={form.place}
                    onChange={e => setForm({ ...form, place: e.target.value })}
                    required
                  />
                </div>
                <div className="event-form-group">
                  <label htmlFor="event-note">Note:</label>
                  <input
                    id="event-note"
                    type="text"
                    value={form.note}
                    onChange={e => setForm({ ...form, note: e.target.value })}
                  />
                </div>
              </div>
              <div className="modal-actions">
                <button type="submit">{editId ? 'Save Changes' : 'Add Event'}</button>
                {editId && (
                  <button type="button" onClick={() => deleteEvent(editId)} style={{ color: 'red' }}>
                    Delete
                  </button>
                )}
                <button type="button" onClick={() => setModalOpen(false)}>Cancel</button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
}

export default App;