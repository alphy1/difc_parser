// ref: https://faun.pub/managing-mongodb-on-docker-with-docker-compose-26bf8a0bbae3

db.createUser(
    {
        user: "username",
        pwd: "password",
        roles: [
            {
                role: "readWrite",
                db: "difc_db",
            }
        ]
    }
)