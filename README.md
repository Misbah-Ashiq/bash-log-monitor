# Bash Log Monitor - Error Filter

This project is a **Bash/Linux task** containerized with **Docker**.\
It scans a given `system.log` file, extracts all lines containing `ERROR`, removes duplicates, and writes the results to `errors.log`.

## 📂 Project Structure

tasks/log-error-filter/
│── Dockerfile # Container setup\
│── solution.sh # Bash script to filter errors\
│── system.log # Sample log file (input)\
│── errors.log # Generated after running solution.sh (output)\
│── run-tests.sh # Test runner\
│── tests/ # Pytest-based validation\
│── task.yaml # Task metadata/config\
│── README.md # Documentation


## 🛠️ How to Build and Run

### 1. Build Docker Image

```bash

docker build -t log-error-filter .

```

### 2. Run Container with Volume Mount

```bash
docker run --rm -it -v $(pwd):/app log-error-filter bash
```

### 3. Run the Script

```bash
./solution.sh
```

Expected output:

```bash
Filtered errors saved to /app/errors.log

```

### 4. Verify Results

```bash
cat errors.log

```

Example output:

```bash
ERROR Connection failed
ERROR Disk full

```

✅ Tests

Run test suite:

```bash
./run-tests.sh

```

All tests must pass before submission.

## 🔧 Technologies Used

- Bash (Linux shell scripting)
- Docker (containerized environment)
- Python + Pytest (for automated testing)

## 📌 Use Cases

- Monitoring and filtering system logs
- DevOps & SysAdmin scripting practice
- Bash/Linux assessment projects

## 🏗️ Architecture

flowchart TD
    A[Developer runs command] --> B[Docker Container]
    B --> C[solution.sh executes]
    C --> D[system.log (input)]
    C --> E[errors.log (output - filtered ERROR lines)]

## 👤 Author

Misbah Ashiq

- 📧 Contact: misbahdevops46@gmail.com
- GitHub: [Misbah-Ashiq](https://github.com/Misbah-Ashiq/Kubernetes-Full-Stack-Project-on-EKS.git)
- Linkedin: [Misbah Ashiq](www.linkedin.com/in/misbah-ashiq-14a0aa356)
- UpWork: [Misbah Ashiq](https://www.upwork.com/freelancers/~0174d196bc738ae9ea)