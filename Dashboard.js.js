import React, { useState } from 'react';
import ReactDOM from 'react-dom';

const Dashboard = () => {
    const [githubUrl, setGithubUrl] = useState('');
    const [githubAccessToken, setGithubAccessToken] = useState('');
    const [username, setUsername] = useState('');

    const handleConfigure = () => {
        // Handle the configuration logic here
        console.log('Configured with:', { githubUrl, githubAccessToken, username });
    };

    return (
        <div>
            <h1>Dashboard Configuration</h1>
            <div>
                <label>
                    GitHub URL:
                    <input
                        type="text"
                        value={githubUrl}
                        onChange={(e) => setGithubUrl(e.target.value)}
                    />
                </label>
            </div>
            <div>
                <label>
                    GitHub Access Token:
                    <input
                        type="text"
                        value={githubAccessToken}
                        onChange={(e) => setGithubAccessToken(e.target.value)}
                    />
                </label>
            </div>
            <div>
                <label>
                    Username:
                    <input
                        type="text"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                    />
                </label>
            </div>
            <button onClick={handleConfigure}>Configure</button>
        </div>
    );
};

ReactDOM.render(<Dashboard />, document.getElementById('root'));