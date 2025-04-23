import React, { useState } from 'react';
import Plot from 'react-plotly.js';
import './Chat.css'; // Ensure you have this CSS file

function Chat() {
    const [query, setQuery] = useState('');
    const [messages, setMessages] = useState([]);
    const [chartData, setChartData] = useState(null);

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (!query) return;

        try {
            const response = await fetch('http://localhost:8000/query', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ query, language: 'en' }),
            });
            const data = await response.json();

            // Log chart data for debugging
            if (data.chart) {
                console.log('Received Chart Data:', data.chart);
            }

            // Add response to messages
            setMessages([...messages, { query, response: data.response, follow_up: data.follow_up }]);

            // Handle chart data
            if (data.chart) {
                console.log('Received Chart Data:', data.chart);
                setChartData(JSON.parse(data.chart));
            } else {
                setChartData(null);
            }

            setQuery('');
        } catch (error) {
            console.error('Error fetching response:', error);
        }
    };

    return (
        <div className="chat-container">
            <div className="messages">
                {messages.map((msg, index) => (
                    <div key={index} className="message">
                        <p><strong>Query:</strong> {msg.query}</p>
                        <p><strong>Response:</strong> {msg.response}</p>
                        <p><strong>Follow-up:</strong> {msg.follow_up}</p>
                    </div>
                ))}
                {chartData && (
                    <div className="chart">
                        <Plot
                            data={chartData.data}
                            layout={{
                                ...chartData.layout,
                                width: 600, // Ensure visible size
                                height: 400,
                                title: chartData.layout.title || 'Trends Over Time',
                            }}
                            config={{ responsive: true }}
                        />
                    </div>
                )}
            </div>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    value={query}
                    onChange={(e) => setQuery(e.target.value)}
                    placeholder="Ask about your analytics data..."
                />
                <button type="submit">Send</button>
            </form>
        </div>
    );
}

export default Chat;