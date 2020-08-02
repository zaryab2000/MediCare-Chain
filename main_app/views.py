import json
from web3 import Web3
from datetime import datetime
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render,redirect,HttpResponse


url = 'https://rpc-mumbai.matic.today'
web3 = Web3(Web3.HTTPProvider(url))
address = web3.toChecksumAddress("0x9354d04e66386693CEAEC931bBDB7b1b369fF1A7")

abi = json.loads('''[
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "previousOwner",
				"type": "address"
			},
			{
				"indexed": true,
				"internalType": "address",
				"name": "newOwner",
				"type": "address"
			}
		],
		"name": "OwnershipTransferred",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "string",
				"name": "name",
				"type": "string"
			},
			{
				"indexed": false,
				"internalType": "address",
				"name": "pid",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "insuredAmount",
				"type": "uint256"
			}
		],
		"name": "newPatientCreated",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "donor",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "address",
				"name": "pid",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "amountReceived",
				"type": "uint256"
			}
		],
		"name": "receivedDonation",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "address",
				"name": "pid",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			}
		],
		"name": "usedInsurance",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "docAddressList",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "doctorCount",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"name": "doctorDetailList",
		"outputs": [
			{
				"internalType": "address",
				"name": "docAdress",
				"type": "address"
			},
			{
				"internalType": "string",
				"name": "docName",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "docSpecialization",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"name": "doctorList",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_pid",
				"type": "address"
			}
		],
		"name": "doctorSign",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_pid",
				"type": "address"
			}
		],
		"name": "donateAmount",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "donationHistoryList",
		"outputs": [
			{
				"internalType": "address",
				"name": "pid",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "donorAddress",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "time",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "patientName",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "donationTransferCount",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "donationTransferList",
		"outputs": [
			{
				"internalType": "address",
				"name": "pid",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "time",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "patientName",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "donorCount",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"name": "donorList",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getBalance",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "owner",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"name": "patientList",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "time",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "insuranceAmount",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "donatedAmount",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "name",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "disease",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "doctorName",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "ipfsHash",
				"type": "string"
			},
			{
				"internalType": "address",
				"name": "doctorAddress",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "patientID",
				"type": "address"
			},
			{
				"internalType": "bool",
				"name": "pidAvailable",
				"type": "bool"
			},
			{
				"internalType": "bool",
				"name": "doctorSignature",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "pidCount",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "pidList",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "renounceOwnership",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_docAddress",
				"type": "address"
			},
			{
				"internalType": "string",
				"name": "_name",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_spec",
				"type": "string"
			}
		],
		"name": "setDoctor",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_name",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_disease",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_ipfsHash",
				"type": "string"
			}
		],
		"name": "setPatientData",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_pid",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "_amountRequired",
				"type": "uint256"
			}
		],
		"name": "transferDonations",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "newOwner",
				"type": "address"
			}
		],
		"name": "transferOwnership",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "withdrawCount",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "withdrawHistoryList",
		"outputs": [
			{
				"internalType": "address",
				"name": "pid",
				"type": "address"
			},
			{
				"internalType": "string",
				"name": "doctorName",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "time",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "patientName",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_pid",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "_amountRequired",
				"type": "uint256"
			}
		],
		"name": "withdrawInsurance",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	}
]''')

contract = web3.eth.contract(address=address,abi=abi)

def owner(request):
	return render(request, 'main_app/admin.html')

def getwithdrawHistory():
	withdrawData = []
	count = contract.functions.withdrawCount().call()
	for i in range(count):
		withdrawl = contract.functions.withdrawHistoryList(i+1).call()
		withdrawData.append(withdrawl)

	return withdrawData


def getDonationHistory():
	donationData = []
	count = contract.functions.donorCount().call()
	for i in range(count):
		donation = contract.functions.donationHistoryList(i+1).call()
		donationData.append(donation)
	return donationData 

def getDoctorId():
	docIds = []
	count = contract.functions.doctorCount().call()
	for i in range(count):
		docId = contract.functions.docAddressList(i+1).call()
		docIds.append(docId)
	return docIds


def getPatientId():
	pidList = []
	count = contract.functions.pidCount().call()
	for i in range(count):
		pids = contract.functions.pidList(i+1).call()
		pidList.append(pids)
	return pidList

def base(request):
	owner = contract.functions.owner().call()
	print(owner)
	doctorList = []
	docIds = getDoctorId()
	for docId in docIds:
		doctor = contract.functions.doctorDetailList(docId).call()
		doctorList.append(doctor)
	
	context = {
		"doctors":doctorList
	}
	return render(request,'main_app/index.html',context)

def patients(request):
	patientsList = []
	docs = getDoctorId()
	pids = getPatientId()
	for pid in pids:
		patient=contract.functions.patientList(pid).call()
		patientsList.append(patient)
	new_list = []
	for data in patientsList:
		old_time = int(data[0])
		real_time = datetime.utcfromtimestamp(old_time).strftime('%Y-%m-%d %H:%M:%S')
		data[0]=real_time
		new_list.append(data)
	# print(new_list)
	context = {
		"patients":new_list,
		"doctors":docs
	}
	return render(request, 'main_app/patients.html',context)


def patientDonation(request):
	patientsList = []
	pids = getPatientId()
	for pid in pids:
		patient=contract.functions.patientList(pid).call()
		patientsList.append(patient)
	new_list = []
	for data in patientsList:
		old_time = int(data[0])
		real_time = datetime.utcfromtimestamp(old_time).strftime('%Y-%m-%d %H:%M:%S')
		data[0]=real_time
		new_list.append(data)
	# print(new_list)
	context = {
		"patients":new_list
	}
	return render(request, 'main_app/patientsDonations.html',context)


def patientDatabase(request):
	patientsList = []
	pids = getPatientId()
	for pid in pids:
		patient=contract.functions.patientList(pid).call()
		patientsList.append(patient)
	new_list = []
	for data in patientsList:
		old_time = int(data[0])
		real_time = datetime.utcfromtimestamp(old_time).strftime('%Y-%m-%d %H:%M:%S')
		data[0]=real_time
		new_list.append(data)
	
	context = {
		"datas":new_list
	}
	return render(request, 'main_app/patientsDataBase.html',context)

def addPatients(request):

	return render(request, 'main_app/addPatients.html')

def addDoctor(request):
	return render(request, 'main_app/addDoctor.html')

def donationData(request):
	new_list = []
	donationData = getDonationHistory()
	for data in donationData:
		old_time = int(data[2])
		real_time = datetime.utcfromtimestamp(old_time).strftime('%Y-%m-%d %H:%M:%S')
		data[2]=real_time
		new_list.append(data)
	
	context = {
		"datas":new_list
	}
	return render(request, 'main_app/donationTable.html',context)

def donationPage(request):
	patientsList = []
	pids = getPatientId()
	for pid in pids:
		patient=contract.functions.patientList(pid).call()
		patientsList.append(patient)
	new_list = []
	for data in patientsList:
		old_time = int(data[0])
		real_time = datetime.utcfromtimestamp(old_time).strftime('%Y-%m-%d %H:%M:%S')
		data[0]=real_time
		new_list.append(data)
	# print(new_list)
	context = {
		"patients":new_list,
		
	}
	return render(request, 'main_app/donateTopatients.html',context)

def withdrawData(request):
	new_list = []
	withdrawData=getwithdrawHistory()
	for data in withdrawData:
		old_time = int(data[2])
		real_time = datetime.utcfromtimestamp(old_time).strftime('%Y-%m-%d %H:%M:%S')
		data[2]=real_time
		new_list.append(data)
	
	context = {
		"datas":new_list
	}
	return render(request, 'main_app/withdrawTable.html',context)

def donate(request,pid):
	context={
		'pid':pid
	}
	return render(request, 'main_app/donation.html',context)

def sign(request,pid):
	patient=contract.functions.patientList(pid).call()
	ipfsHash = patient[6]
	docs = getDoctorId()
	
	context={
		'pid':pid,
		'ipfsHash':ipfsHash,
		'doctors':docs
	}
	return render(request, 'main_app/sign.html',context)

def withdrawAmount(request, pid):
	context={
		'pid':pid
	}
	return render(request, 'main_app/withdrawAmount.html', context)

def transferDonation(request,pid):
	context={
		'pid':pid
	}
	return render(request, 'main_app/transferDonation.html', context)


def errorPage(request):
	return render(request, 'main_app/errorPage.html')