const userModel = require("../models/userModels");
const bcrypt = require("bcryptjs");
const jwt = require("jsonwebtoken");
const doctorModel = require("../models/doctorModel");
const appointmentModel = require("../models/appointmentModel");
const moment = require("moment");

// Register callback
const registerController = async (req, res) => {
  try {
    const existingUser = await userModel.findOne({ email: req.body.email });
    if (existingUser) {
      return res.status(409).send({ message: "User already exists", success: false });
    }
    const salt = await bcrypt.genSalt(10);
    const hashedPassword = await bcrypt.hash(req.body.password, salt);
    const newUser = new userModel({ ...req.body, password: hashedPassword });
    await newUser.save();
    res.status(201).send({ message: "Registered successfully", success: true });
  } catch (error) {
    console.error(error);
    res.status(500).send({ success: false, message: `Register Controller: ${error.message}` });
  }
};

// Login callback
const loginController = async (req, res) => {
  try {
    const user = await userModel.findOne({ email: req.body.email });
    if (!user) {
      return res.status(404).send({ message: "User not found", success: false });
    }
    const isMatch = await bcrypt.compare(req.body.password, user.password);
    if (!isMatch) {
      return res.status(400).send({ message: "Invalid email or password", success: false });
    }
    const token = jwt.sign({ id: user._id }, process.env.JWT_SECRET, { expiresIn: "1d" });
    res.status(200).send({ message: "Login successful", success: true, token });
  } catch (error) {
    console.error(error);
    res.status(500).send({ message: `Error in Login Controller: ${error.message}` });
  }
};

// Auth callback
const authController = async (req, res) => {
  try {
    const user = await userModel.findById(req.body.userId).select('-password');
    if (!user) {
      return res.status(404).send({ message: "User not found", success: false });
    }
    res.status(200).send({ success: true, data: user });
  } catch (error) {
    console.error(error);
    res.status(500).send({ message: "Auth error", success: false, error });
  }
};

// Apply doctor callback
const applyDoctorController = async (req, res) => {
  try {
    const newDoctor = new doctorModel({ ...req.body, status: "pending" });
    await newDoctor.save();

    const adminUser = await userModel.findOne({ isAdmin: true });
    if (adminUser) {
      adminUser.notification.push({
        type: "apply-doctor-request",
        message: `${newDoctor.firstName} ${newDoctor.lastName} has applied for a doctor account.`,
        data: {
          doctorId: newDoctor._id,
          name: `${newDoctor.firstName} ${newDoctor.lastName}`,
          onClickPath: "/admin/doctors",
        },
      });
      await adminUser.save();
    }

    res.status(201).send({ success: true, message: "Doctor account applied successfully" });
  } catch (error) {
    console.error(error);
    res.status(500).send({ success: false, error, message: "Error while applying for doctor" });
  }
};

// Get all notifications callback
const getAllNotificationController = async (req, res) => {
  try {
    const user = await userModel.findById(req.body.userId);
    if (!user) {
      return res.status(404).send({ message: "User not found", success: false });
    }
    user.seenNotification.push(...user.notification);
    user.notification = [];
    await user.save();
    res.status(200).send({ success: true, message: "All notifications marked as read", data: user });
  } catch (error) {
    console.error(error);
    res.status(500).send({ message: "Error in notification", success: false, error });
  }
};

// Delete all notifications callback
const deleteAllNotificationController = async (req, res) => {
  try {
    const user = await userModel.findById(req.body.userId);
    if (!user) {
      return res.status(404).send({ message: "User not found", success: false });
    }
    user.notification = [];
    user.seenNotification = [];
    await user.save();
    res.status(200).send({ success: true, message: "Notifications deleted successfully", data: user });
  } catch (error) {
    console.error(error);
    res.status(500).send({ success: false, message: "Unable to delete all notifications", error });
  }
};

// Get all doctors callback
const getAllDoctorsController = async (req, res) => {
  try {
    const doctors = await doctorModel.find({ status: "approved" });
    res.status(200).send({ success: true, message: "Doctor list fetched successfully", data: doctors });
  } catch (error) {
    console.error(error);
    res.status(500).send({ success: false, error, message: "Error while fetching doctors" });
  }
};

// Book appointment callback
const bookAppointmentController = async (req, res) => {
  try {
    req.body.date = moment(req.body.date, "DD-MM-YYYY").toISOString();
    req.body.time = moment(req.body.time, "HH:mm").toISOString();
    req.body.status = "pending";
    const newAppointment = new appointmentModel(req.body);
    await newAppointment.save();

    const doctorUser = await userModel.findById(req.body.doctorInfo.userId);
    if (doctorUser) {
      doctorUser.notification.push({
        type: "new-appointment-request",
        message: `A new appointment request from ${req.body.userInfo.name}`,
        onClickPath: "/user/appointments",
      });
      await doctorUser.save();
    }

    res.status(200).send({ success: true, message: "Appointment booked successfully" });
  } catch (error) {
    console.error(error);
    res.status(500).send({ success: false, error, message: "Error while booking appointment" });
  }
};

// Booking availability callback
const bookingAvailabilityController = async (req, res) => {
  try {
    const date = moment(req.body.date, "DD-MM-YYYY").toISOString();
    const fromTime = moment(req.body.time, "HH:mm").subtract(1, "hour").toISOString();
    const toTime = moment(req.body.time, "HH:mm").add(1, "hour").toISOString();
    const doctorId = req.body.doctorId;

    const appointments = await appointmentModel.find({
      doctorId,
      date,
      time: { $gte: fromTime, $lte: toTime }
    });

    if (appointments.length > 0) {
      return res.status(409).send({ message: "Appointments not available at this time", success: false });
    }

    res.status(200).send({ success: true, message: "Appointments available" });
  } catch (error) {
    console.error(error);
    res.status(500).send({ success: false, error, message: "Error in booking availability" });
  }
};

// Get user appointments callback
const userAppointmentsController = async (req, res) => {
  try {
    const appointments = await appointmentModel.find({ userId: req.body.userId });
    res.status(200).send({ success: true, message: "User appointments fetched successfully", data: appointments });
  } catch (error) {
    console.error(error);
    res.status(500).send({ success: false, error, message: "Error in fetching user appointments" });
  }
};

module.exports = {
  loginController,
  registerController,
  authController,
  applyDoctorController,
  getAllNotificationController,
  deleteAllNotificationController,
  getAllDoctorsController,
  bookAppointmentController,
  bookingAvailabilityController,
  userAppointmentsController,
};
