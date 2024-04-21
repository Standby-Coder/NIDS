const express = require("express");
const cors = require("cors");
const mongoose = require("mongoose");
const authRoutes = require("./Routes/authRoutes");

require('dotenv').config();

const app = express();
app.listen(process.env.PORT, () => {
    console.log(`Server Started Successfully on ${process.env.PORT}.`);
}
);
mongoose
    .connect(process.env.MONGO_URI, {
        useNewUrlParser: true,
        useUnifiedTopology: true,
    })
    .then(() => {
        console.log("DB Connetion Successfull");
    })
    .catch((err) => {
        console.log(err.message);
    });

app.use(cors());
app.use(express.json());
app.use('/', authRoutes);
